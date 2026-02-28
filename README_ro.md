# 💀 HADES
### Hard Disk Explorer & Storage

> *"O după-amiază de sâmbătă. Un actor. Un laptop. Nimic mai bun de făcut."*

---

## Ce este asta?

HADES este un sistem de indexare a discurilor care știe exact ce se află pe hard disk-urile tale externe — probabil mai bine decât tine.

Scanează, urmărește versiuni, detectează modificări și aruncă totul într-un fișier Excel frumos. De ce nu?

---

## Ce poate face?

- 🔍 **Detectare automată a discurilor** – conectează-l, HADES observă
- 📁 **Index de fișiere** – fiecare fișier, fiecare disc, într-un singur loc
- 🔄 **Urmărirea modificărilor** – știe ce era, ce este acum, ce a dispărut
- 📊 **Export Excel** – Dashboard + foi individuale per disc
- ⚡ **Cache inteligent** – dacă nu s-a schimbat nimic, nu se regenerează nimic (pentru că recitirea a 296k fișiere nu e sport)
- 💾 **Baza de date SQLite** – persistentă, robustă, nu uită niciodată

---

## Instalare

```bash
git clone https://github.com/ferkomatolcsi-coder/HADES.git
cd HADES
pip install -r requirements.txt
```

---

## Utilizare

**Scanare** – indexează discurile conectate:
```bash
python3 hades_scan.py
```

**Export** – generează fișierul Excel:
```bash
python3 hades_export.py
```

Rezultat: `HADES_export_DATA_ORA.xlsx` în folderul HADES.

---

## Cerințe

- Python 3.8+
- macOS sau Linux
- Cel puțin un disc extern la care nu te-ai uitat de ceva vreme

---

## Compatibilitate

| Platformă | Status |
|-----------|--------|
| macOS     | ✅ Testat |
| Linux     | ✅ Suportat |
| Windows   | 🤷 Poate cândva |

---

## Roadmap

- [ ] Interfață web (dashboard bazat pe Flask)
- [ ] Auto-scanare GitHub Actions
- [ ] Suport Windows
- [ ] Poate să dormim sâmbăta

---

## Autor

**ferkomatolcsi-coder** – actor, dezvoltator, bricoleur de sâmbătă.  
N-a plănuit să facă un proiect. S-a întâmplat și gata.

---

*Built with Passion* 🔥  
*(și destulă cafea)*
