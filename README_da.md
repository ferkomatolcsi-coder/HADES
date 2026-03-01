# 💀 HADES
### Hard Disk Explorer & Storage

> *"En lørdag eftermiddag. En skuespiller. En laptop. Intet bedre at lave."*

---

## Hvad er det her?

HADES er et diskindekseringssystem der ved præcis hvad der er på dine eksterne harddiske — sandsynligvis bedre end du selv gør.

Det scanner, sporer versioner, opdager ændringer og spytter det hele ud i en flot Excel-fil. Fordi hvorfor ikke.

---

## Hvad kan det?

- 🔍 **Automatisk diskgenkendelse** – tilslut den, HADES bemærker det
- 📁 **Filindeks** – hver fil, hver disk, ét sted
- 🔄 **Ændringssporing** – ved hvad der var, hvad der er nu, hvad der forsvandt
- 📊 **Excel-eksport** – Dashboard + individuelle ark per disk
- ⚡ **Smart cache** – hvis intet er ændret, genereres intet om (for at genlæse 296k filer er ingen sport)
- 💾 **SQLite-database** – persistent, robust, glemmer aldrig

---

## Installation

```bash
git clone https://github.com/ferkomatolcsi-coder/HADES.git
cd HADES
pip install -r requirements.txt
```

---

## Brug

**Scan** – indekserer tilsluttede diske:
```bash
python3 hades_scan.py
```

**Eksport** – genererer Excel-filen:
```bash
python3 hades_export.py
```

Resultat: `HADES_export_DATO_TID.xlsx` i HADES-mappen.

---

## Krav

- Python 3.8+
- macOS eller Linux
- Mindst én ekstern disk du ikke har kigget på i et stykke tid

---

## Kompatibilitet

| Platform | Status |
|----------|--------|
| macOS    | ✅ Testet |
| Linux    | ✅ Understøttet |
| Windows  | 🤷 Måske en dag |

---

## Roadmap

- [ ] Web-UI (Flask-baseret dashboard)
- [ ] GitHub Actions auto-scan
- [ ] Windows-support
- [ ] Måske sove om lørdagen

---

## Forfatter

**ferkomatolcsi-coder** – skuespiller, udvikler, lørdagspjusker.  
Planlagde ikke at lave et projekt. Det skete bare.

---

*Built with Passion* 🔥  
*(og en ordentlig mængde kaffe)*
