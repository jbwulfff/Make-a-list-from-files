# 🧾 Make-a-list-from-files

Et Python-script, der samler alle tekst- og kodefiler fra en mappe og dens undermapper i ét markdown-dokument – perfekt til dokumentation, arkivering eller kodegennemgang.

---

## 📦 Funktioner

- Gennemgår mapper rekursivt
- Samler tekst- og kodefiler i én markdown-fil
- Tilføjer filstier og korrekte markdown-kodeblokke baseret på filtype
- Understøtter:
  - udelukkelse af bestemte filendelser
  - filtrering så kun bestemte typer filer inkluderes
  - udeladelse af bestemte undermapper

---

## 🛠️ Krav

- Python 3.x

---

## 🚀 Brug

```bash
python3 concat_files.py path/to/input_folder -o output.md
