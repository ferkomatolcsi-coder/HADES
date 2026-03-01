# 💀 HADES
### Hard Disk Explorer & Storage

> *"A Saturday afternoon. An actor. A laptop. Nothing better to do."*

---

## What is this?

HADES is a disk indexing system that knows exactly what's on your external hard drives — probably better than you do.

It scans, tracks versions, detects changes, and spits it all out into a beautiful Excel file. Because why not.

---

## What can it do?

- 🔍 **Automatic disk detection** – plug it in, HADES notices
- 📁 **File index** – every file, every disk, in one place
- 🔄 **Change tracking** – knows what was there, what's there now, what vanished
- 📊 **Excel export** – Dashboard + individual sheets per disk
- ⚡ **Smart cache** – if nothing changed, nothing gets regenerated (because re-reading 296k files is not a sport)
- 💾 **SQLite database** – persistent, robust, never forgets

---

## Installation

```bash
git clone https://github.com/ferkomatolcsi-coder/HADES.git
cd HADES
pip install -r requirements.txt
```

---

## Usage

**Scan** – indexes connected disks:
```bash
python3 hades_scan.py
```

**Export** – generates the Excel file:
```bash
python3 hades_export.py
```

Result: `HADES_export_DATE_TIME.xlsx` in the HADES folder.

---

## Requirements

- Python 3.8+
- macOS or Linux
- At least one external disk you haven't looked at in a while

---

## Compatibility

| Platform | Status |
|----------|--------|
| macOS    | ✅ Tested |
| Linux    | ✅ Supported |
| Windows  | 🤷 Maybe someday |

---

## Roadmap

- [ ] Web UI (Flask-based dashboard)
- [ ] GitHub Actions auto-scan
- [ ] Windows support
- [ ] Maybe sleep on Saturdays

---

## Author

**ferkomatolcsi-coder** – actor, developer, Saturday tinkerer.  
Didn't plan to make a project. It just happened.

---

*Built with Passion* 🔥  
*(and a fair amount of coffee)*
