"""
HADES v2 - hades_scan.py
Mount detect + file indexer + diff trigger
Cross-platform: Darwin (macOS) / Linux
"""

import os
import sys
import platform
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from hades_db import (
    init_db, get_or_create_disk, get_last_version,
    get_version_files, compute_diff, save_new_version
)

SCAN_DEPTH = 7
EXCLUDE_DIRS = {".Trashes", ".Spotlight-V100"}

def get_platform():
    return "darwin" if platform.system() == "Darwin" else "linux"

def get_mount_root():
    if get_platform() == "darwin":
        return Path("/Volumes")
    user = os.environ.get("USER", "")
    media = Path(f"/media/{user}")
    return media if media.exists() else Path("/mnt")

def detect_disks():
    mount_root = get_mount_root()
    found = []
    if not mount_root.exists():
        return found
    for entry in mount_root.iterdir():
        if entry.name in ["Macintosh HD", "Recovery", "VM", "Preboot", "Data"]:
            continue
        if entry.is_dir():
            found.append({"label": entry.name, "mount_point": entry, "platform": get_platform()})
    return found

def scan_files(mount_point, max_depth=SCAN_DEPTH):
    files = {}
    skipped = 0
    mount_str = str(mount_point)
    def _scan(path, depth):
        nonlocal skipped
        if depth > max_depth:
            return
        try:
            for entry in path.iterdir():
                try:
                    if entry.is_symlink():
                        continue
                    if entry.is_dir():
                        if entry.name in EXCLUDE_DIRS:
                            skipped += 1
                            continue
                        _scan(entry, depth + 1)
                    elif entry.is_file():
                        rel_path = str(entry).replace(mount_str, "")
                        stat = entry.stat()
                        files[rel_path] = {"size": stat.st_size, "modified": datetime.fromtimestamp(stat.st_mtime).isoformat()}
                except (PermissionError, OSError):
                    pass
        except PermissionError:
            pass
    _scan(mount_point, 0)
    if skipped:
        print(f"[HADES] Skipped {skipped} excluded dirs {EXCLUDE_DIRS}")
    return files

def format_bytes(b):
    for unit in ["B","KB","MB","GB","TB"]:
        if b < 1024:
            return f"{b:.1f} {unit}"
        b /= 1024

def run_scan(label=None):
    init_db()
    plat = get_platform()
    print(f"\n[HADES] Platform: {plat.upper()}")
    print(f"[HADES] Detecting disks...\n")
    disks = detect_disks()
    if not disks:
        print("[HADES] No external disks found.")
        return
    if label:
        disks = [d for d in disks if d["label"].upper() == label.upper()]
        if not disks:
            print(f"[HADES] Disk not found: {label}")
            return
    for disk in disks:
        print(f"{'='*50}")
        print(f"💾 {disk['label']} @ {disk['mount_point']}")
        print(f"{'='*50}")
        disk_id = get_or_create_disk(label=disk["label"], platform=plat)
        print(f"[HADES] Scanning... (max depth: {SCAN_DEPTH})")
        start = datetime.now()
        files = scan_files(disk["mount_point"])
        elapsed = (datetime.now() - start).total_seconds()
        total_size = sum(f["size"] for f in files.values())
        print(f"[HADES] Found {len(files)} files | {format_bytes(total_size)} | {elapsed:.1f}s")
        last = get_last_version(disk_id)
        if last is None:
            print(f"[HADES] First scan - no previous version.")
            diff = {"added": list(files.keys()), "removed": [], "modified": [], "has_changes": True}
            save_new_version(disk_id, files, diff, prev_version_id=None)
            print(f"[HADES] ✅ Initial version saved.")
        else:
            print(f"[HADES] Previous: {last['scanned_at'][:19]} | {last['file_count']} files")
            old_files = get_version_files(last["id"])
            diff = compute_diff(old_files, files)
            if diff["has_changes"]:
                print(f"[HADES] Changes: +{len(diff['added'])} -{len(diff['removed'])} ~{len(diff['modified'])}")
                save_new_version(disk_id, files, diff, prev_version_id=last["id"])
                print(f"[HADES] ✅ New version saved.")
            else:
                print(f"[HADES] ✅ No changes - skip.")
        print()

if __name__ == "__main__":
    run_scan(sys.argv[1] if len(sys.argv) > 1 else None)
