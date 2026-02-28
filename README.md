# 💀 HADES
### Hard Disk Explorer & Storage

---

🇭🇺 [Magyar](README_hu.md) · 🇬🇧 [English](README_en.md) · 🇸🇪 [Svenska](README_sv.md) · 🇩🇰 [Dansk](README_da.md) · 🇮🇪 [Gaeilge](README_ga.md) · 🇷🇴 [Română](README_ro.md) · 🇰🇷 [한국어](README_ko.md) · 🇯🇵 [日本語](README_ja.md) · 🇸🇦 [العربية](README_ar.md)

---

> *"Egy szombat délután. Egy színész. Egy laptop. Semmi jobb dolguk nem volt."*

---

## Mi ez?

HADES egy lemezindexelő rendszer, ami pontosan tudja mi van a külső merevlemezeiden – még te sem tudod annyira jól.

Scannel, verziókövet, változást detektál, és az egészet kiköpi egy szép Excel fájlba. Mert miért ne.

---

## Mit tud?

- 🔍 **Automatikus lemezfelismerés** – bedugod, észreveszi
- 📁 **Fájlindex** – minden fájl, minden lemez, egy helyen
- 🔄 **Változáskövetés** – tudja mi volt, mi lett, mi tűnt el
- 📊 **Excel export** – Dashboard + lemezenkénti sheetek
- ⚡ **Smart cache** – ha nem változott semmi, nem generál újra feleslegesen (mert 296k fájlt újraolvasni nem sport)
- 💾 **SQLite adatbázis** – perzisztens, robusztus, nem felejt

---

## Telepítés

```bash
git clone https://github.com/ferkomatolcsi-coder/HADES.git
cd HADES
pip install -r requirements.txt
```

---

## Használat

**Scan** – indexeli a csatlakoztatott lemezeket:
```bash
python3 hades_scan.py
```

**Export** – generálja az Excel fájlt:
```bash
python3 hades_export.py
```

Az eredmény: `HADES_export_DÁTUM_IDŐ.xlsx` a HADES mappában.

---

## Rendszerkövetelmények

- Python 3.8+
- macOS vagy Linux
- Legalább egy külső lemez amit már rég nem nézett meg az ember

---

## Kompatibilitás

| Platform | Státusz |
|----------|---------|
| macOS    | ✅ Tesztelve |
| Linux    | ✅ Támogatott |
| Windows  | 🤷 Talán egyszer |

---

## Roadmap

- [ ] Web UI (Flask alapú dashboard)
- [ ] GitHub Actions auto-scan
- [ ] Windows support
- [ ] Esetleg alvás is szombaton

---

## Szerző

**ferkomatolcsi-coder** – színész, informatikus, szombati barkácsoló.  
Nem tervezett projektet csinálni. Csak úgy eszébe jutott.

---

*Built with Passion* 🔥  
*(és egy adag kávé)*
