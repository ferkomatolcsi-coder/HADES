"""
HADES v2 - hades_db.py
Core SQLite database module Omg hogy miket csinálok:)
Personal file indexer - persistent + version history
"""

import sqlite3
import os
import shutil
from datetime import datetime
from pathlib import Path

# --- Config ---
HADES_DIR = Path.home() / "Desktop" / "HADES"
DB_PATH = HADES_DIR / "hades.db"
BACKUP_DIR = HADES_DIR / "db_backup"
DB_PATH = HADES_DIR / "hades.db"
MAX_VERSIONS_PER_DISK = 3
MAX_BACKUPS = 4


def init_db():
    """Create DB and schema if not exists."""
    HADES_DIR.mkdir(parents=True, exist_ok=True)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()

    c.executescript("""
        CREATE TABLE IF NOT EXISTS disks (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            label       TEXT UNIQUE NOT NULL,
            serial      TEXT,
            platform    TEXT,
            last_seen   TEXT
        );

        CREATE TABLE IF NOT EXISTS scan_versions (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            disk_id     INTEGER NOT NULL REFERENCES disks(id) ON DELETE CASCADE,
            scanned_at  TEXT NOT NULL,
            file_count  INTEGER DEFAULT 0,
            total_bytes INTEGER DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS files (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            version_id  INTEGER NOT NULL REFERENCES scan_versions(id) ON DELETE CASCADE,
            path        TEXT NOT NULL,
            size_bytes  INTEGER DEFAULT 0,
            modified_at TEXT
        );

        CREATE TABLE IF NOT EXISTS diff_log (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            disk_id     INTEGER NOT NULL REFERENCES disks(id) ON DELETE CASCADE,
            from_ver    INTEGER,
            to_ver      INTEGER NOT NULL,
            added       INTEGER DEFAULT 0,
            removed     INTEGER DEFAULT 0,
            modified    INTEGER DEFAULT 0,
            logged_at   TEXT NOT NULL
        );
    """)

    conn.commit()
    conn.close()
    print(f"[HADES] DB initialized: {DB_PATH}")


def rotate_backup():
    """Rotate backup files: bak4 drop, bak3->bak4, ..., db->bak1"""
    bak = [BACKUP_DIR / f"hades.db.bak{i}" for i in range(1, MAX_BACKUPS + 1)]

    # Drop oldest
    if bak[3].exists():
        bak[3].unlink()
        print(f"[HADES] Dropped: {bak[3].name}")

    # Rotate: bak3->bak4, bak2->bak3, bak1->bak2
    for i in range(MAX_BACKUPS - 1, 0, -1):
        if bak[i - 1].exists():
            bak[i - 1].rename(bak[i])
            print(f"[HADES] Rotated: {bak[i-1].name} → {bak[i].name}")

    # Current DB -> bak1
    if DB_PATH.exists():
        shutil.copy2(DB_PATH, bak[0])
        print(f"[HADES] Backup created: {bak[0].name}")


def get_or_create_disk(label: str, serial: str = None, platform: str = None) -> int:
    """Return disk id, create if not exists."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()

    now = datetime.now().isoformat()
    c.execute("SELECT id FROM disks WHERE label = ?", (label,))
    row = c.fetchone()

    if row:
        disk_id = row[0]
        c.execute("UPDATE disks SET last_seen=?, serial=COALESCE(?,serial), platform=COALESCE(?,platform) WHERE id=?",
                  (now, serial, platform, disk_id))
    else:
        c.execute("INSERT INTO disks (label, serial, platform, last_seen) VALUES (?,?,?,?)",
                  (label, serial, platform, now))
        disk_id = c.lastrowid
        print(f"[HADES] New disk registered: {label} (id={disk_id})")

    conn.commit()
    conn.close()
    return disk_id


def get_last_version(disk_id: int) -> dict | None:
    """Return latest scan version for disk, or None."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        SELECT id, scanned_at, file_count, total_bytes
        FROM scan_versions
        WHERE disk_id = ?
        ORDER BY scanned_at DESC
        LIMIT 1
    """, (disk_id,))
    row = c.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "scanned_at": row[1], "file_count": row[2], "total_bytes": row[3]}
    return None


def get_version_files(version_id: int) -> dict:
    """Return {path: {size, modified}} for a version."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT path, size_bytes, modified_at FROM files WHERE version_id = ?", (version_id,))
    result = {row[0]: {"size": row[1], "modified": row[2]} for row in c.fetchall()}
    conn.close()
    return result


def compute_diff(old_files: dict, new_files: dict) -> dict:
    """Compare two file dicts, return diff summary."""
    old_paths = set(old_files.keys())
    new_paths = set(new_files.keys())

    added = new_paths - old_paths
    removed = old_paths - new_paths
    common = old_paths & new_paths
    modified = {
        p for p in common
        if old_files[p]["size"] != new_files[p]["size"]
        or old_files[p]["modified"] != new_files[p]["modified"]
    }

    return {
        "added": list(added),
        "removed": list(removed),
        "modified": list(modified),
        "has_changes": bool(added or removed or modified)
    }


def save_new_version(disk_id: int, files: dict, diff: dict, prev_version_id: int = None):
    """Save new scan version, prune old ones, rotate backup."""
    rotate_backup()

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()
    now = datetime.now().isoformat()

    total_bytes = sum(f["size"] for f in files.values())

    # Insert new version
    c.execute("""
        INSERT INTO scan_versions (disk_id, scanned_at, file_count, total_bytes)
        VALUES (?,?,?,?)
    """, (disk_id, now, len(files), total_bytes))
    new_ver_id = c.lastrowid

    # Insert files
    c.executemany("""
        INSERT INTO files (version_id, path, size_bytes, modified_at)
        VALUES (?,?,?,?)
    """, [(new_ver_id, path, meta["size"], meta["modified"]) for path, meta in files.items()])

    # Log diff
    c.execute("""
        INSERT INTO diff_log (disk_id, from_ver, to_ver, added, removed, modified, logged_at)
        VALUES (?,?,?,?,?,?,?)
    """, (disk_id, prev_version_id, new_ver_id,
          len(diff["added"]), len(diff["removed"]), len(diff["modified"]), now))

    # Prune: keep only MAX_VERSIONS_PER_DISK newest
    c.execute("""
        SELECT id FROM scan_versions WHERE disk_id = ?
        ORDER BY scanned_at DESC
    """, (disk_id,))
    all_versions = [row[0] for row in c.fetchall()]

    to_delete = all_versions[MAX_VERSIONS_PER_DISK:]
    for vid in to_delete:
        c.execute("DELETE FROM scan_versions WHERE id = ?", (vid,))
        print(f"[HADES] Pruned old version: id={vid}")

    conn.commit()
    conn.close()
    print(f"[HADES] New version saved: id={new_ver_id} | +{len(diff['added'])} -{len(diff['removed'])} ~{len(diff['modified'])}")
    return new_ver_id


def status():
    """Print current DB status."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("SELECT id, label, platform, last_seen FROM disks")
    disks = c.fetchall()

    print("\n=== HADES DB STATUS ===")
    for disk in disks:
        disk_id, label, platform, last_seen = disk
        c.execute("""
            SELECT id, scanned_at, file_count, total_bytes
            FROM scan_versions WHERE disk_id = ?
            ORDER BY scanned_at DESC
        """, (disk_id,))
        versions = c.fetchall()
        print(f"\n💾 {label} [{platform}] | last seen: {last_seen}")
        for v in versions:
            gb = v[3] / (1024**3)
            print(f"   v{v[0]} | {v[1][:19]} | {v[2]} files | {gb:.2f} GB")

    # Backups
    print("\n📦 Backups:")
    for i in range(1, MAX_BACKUPS + 1):
        bak = BACKUP_DIR / f"hades.db.bak{i}"
        if bak.exists():
            size_kb = bak.stat().st_size / 1024
            print(f"   bak{i}: {size_kb:.1f} KB")
        else:
            print(f"   bak{i}: —")

    conn.close()
    print()


# --- DEMO / TEST ---
if __name__ == "__main__":
    print("=== HADES DB - Init & Demo ===\n")
    init_db()

    # Simulate GRANIT disk - first scan
    disk_id = get_or_create_disk("GRANIT", serial="SN-001", platform="darwin")

    fake_scan_1 = {
        "/Volumes/GRANIT/Photos/img001.jpg": {"size": 3_200_000, "modified": "2024-01-10T10:00:00"},
        "/Volumes/GRANIT/Photos/img002.jpg": {"size": 2_800_000, "modified": "2024-01-11T11:00:00"},
        "/Volumes/GRANIT/Docs/notes.txt":    {"size": 12_000,    "modified": "2024-03-01T09:00:00"},
    }

    last = get_last_version(disk_id)
    if last is None:
        print("[HADES] First scan - no previous version, saving...")
        diff = {"added": list(fake_scan_1.keys()), "removed": [], "modified": [], "has_changes": True}
        save_new_version(disk_id, fake_scan_1, diff, prev_version_id=None)
    else:
        old_files = get_version_files(last["id"])
        diff = compute_diff(old_files, fake_scan_1)
        if diff["has_changes"]:
            save_new_version(disk_id, fake_scan_1, diff, prev_version_id=last["id"])
        else:
            print("[HADES] No changes detected - skip.")

    # Simulate second scan with changes
    print("\n--- Simulating second scan with changes ---")
    fake_scan_2 = {
        "/Volumes/GRANIT/Photos/img001.jpg": {"size": 3_200_000, "modified": "2024-01-10T10:00:00"},
        "/Volumes/GRANIT/Photos/img003.jpg": {"size": 4_100_000, "modified": "2024-06-01T15:00:00"},  # new
        "/Volumes/GRANIT/Docs/notes.txt":    {"size": 15_000,    "modified": "2024-06-15T12:00:00"},  # modified
        # img002 removed
    }

    last = get_last_version(disk_id)
    old_files = get_version_files(last["id"])
    diff = compute_diff(old_files, fake_scan_2)
    if diff["has_changes"]:
        print(f"[HADES] Changes: +{len(diff['added'])} added, -{len(diff['removed'])} removed, ~{len(diff['modified'])} modified")
        save_new_version(disk_id, fake_scan_2, diff, prev_version_id=last["id"])
    else:
        print("[HADES] No changes - skip.")

    status()
