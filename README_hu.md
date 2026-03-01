# 💀 HADES
## Hard Disk Explorer & Storage

> *"Egy szombat délután. Egy színész. Egy laptop. Semmi jobb teendő."*

---

## Mi ez?

A HADES egy lemezindexelő rendszer, amely pontosan tudja mi van a külső merevlemezeiden – valószínűleg jobban, mint te.

Átvizsgál, verziókat követ, változásokat érzékel, és mindezt egy gyönyörű Excel fájlba köpi ki. Mert miért ne.

---

## Mit tud?

- 🔍 **Automatikus lemezfelismerés** – bedugod, a HADES észreveszi
- 📁 **Fájlindex** – minden fájl, minden lemez, egy helyen
- 🔄 **Változáskövetés** – tudja mi volt ott, mi van ott most, mi tűnt el
- 📊 **Excel export** – Dashboard + külön lapok lemezenként
- ⚡ **Okos cache** – ha semmi sem változott, semmi sem generálódik újra *(mert 296 ezer fájlt újraolvasni nem sport)*
- 💾 **SQLite adatbázis** – tartós, robusztus, soha nem felejt

---

## Telepítés

```bash
git clone https://github.com/ferkomatolcsi-coder/HADES.git
cd HADES
pip install -r requirements.txt
```

---

## Használat

**Szkennelés** – indexeli a csatlakoztatott lemezeket:

```bash
python3 hades_scan.py
```

**Export** – legenerálja az Excel fájlt:

```bash
python3 hades_export.py
```

Eredmény: `HADES_export_DÁTUM_IDŐ.xlsx` a HADES mappában.

---

## Követelmények

- Python 3.8+
- macOS vagy Linux
- Legalább egy külső lemez, amelyre egy ideje nem nézett rá

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
- [ ] Windows támogatás
- [ ] Talán aludni szombatonként

---

## Szerző

**ferkomatolcsi-coder** – színész, fejlesztő, szombati barkácsoló.
Nem tervezett projektet csinálni. Csak megtörtént.

---

*Szenvedéllyel építve 🔥 (és nem kevés kávéval)*
