# 💀 HADES
### Hard Disk Explorer & Storage

> *"En lördagseftermiddag. En skådespelare. En laptop. Ingenting bättre att göra."*

---

## Vad är det här?

HADES är ett diskindexeringssystem som vet exakt vad som finns på dina externa hårddiskar — förmodligen bättre än du själv.

Det skannar, spårar versioner, detekterar ändringar och spottar ut alltihop i en snygg Excel-fil. För varför inte.

---

## Vad kan det göra?

- 🔍 **Automatisk diskidentifiering** – anslut den, HADES märker det
- 📁 **Filindex** – varje fil, varje disk, på ett ställe
- 🔄 **Ändringsspårning** – vet vad som fanns, vad som finns nu, vad som försvann
- 📊 **Excel-export** – Dashboard + individuella flikar per disk
- ⚡ **Smart cache** – om inget ändrats regenereras ingenting (för att läsa om 296k filer är ingen sport)
- 💾 **SQLite-databas** – persistent, robust, glömmer aldrig

---

## Installation

```bash
git clone https://github.com/ferkomatolcsi-coder/HADES.git
cd HADES
pip install -r requirements.txt
```

---

## Användning

**Skanna** – indexerar anslutna diskar:
```bash
python3 hades_scan.py
```

**Exportera** – genererar Excel-filen:
```bash
python3 hades_export.py
```

Resultat: `HADES_export_DATUM_TID.xlsx` i HADES-mappen.

---

## Krav

- Python 3.8+
- macOS eller Linux
- Minst en extern disk du inte kollat på på ett tag

---

## Kompatibilitet

| Plattform | Status |
|-----------|--------|
| macOS     | ✅ Testad |
| Linux     | ✅ Stöds |
| Windows   | 🤷 Kanske en dag |

---

## Roadmap

- [ ] Webb-UI (Flask-baserad dashboard)
- [ ] GitHub Actions auto-skanning
- [ ] Windows-stöd
- [ ] Kanske sova på lördagar

---

## Skapare

**ferkomatolcsi-coder** – skådespelare, utvecklare, lördagspysslare.  
Planerade inte att göra ett projekt. Det bara hände.

---

*Built with Passion* 🔥  
*(och en rejäl dos kaffe)*
