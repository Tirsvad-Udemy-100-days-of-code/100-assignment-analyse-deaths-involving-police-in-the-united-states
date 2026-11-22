[English](Home) · [Dansk](Home-da) · **Bahasa Malaysia**

# Wiki Fatal Force

Wiki ini menerangkan apa yang diajar oleh setiap langkah kuliah dalam tugasan Hari 100 kursus Udemy *100 Days of Code: The Complete Python Pro Bootcamp*. Projek ini menganalisis pangkalan data Washington Post tentang tembakan maut polis bersama data banci Amerika Syarikat dalam buku nota Jupyter yang disokong pakej Python kecil yang diuji.

Topiknya sensitif. Carta menunjukkan bilangan dan kadar, bukan sebab; setiap halaman menyatakan had cartanya.

## Jalankannya

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[analysis,dev]"
python -m pytest
jupyter lab src/notebooks/fatal_force.ipynb
```

Salin fail CSV kursus ke folder `data/` dahulu (lihat README).

## Halaman

- [Langkah 1 dan 2: penerokaan dan pembersihan data](Data-Exploration-and-Cleaning-ms)
- [Langkah 3 hingga 6: kemiskinan dan tamat sekolah menengah](Poverty-and-Graduation-ms)
- [Langkah 7 dan 8: komposisi kaum dan kematian mengikut kaum](Racial-Demographics-ms)
- [Langkah 9 hingga 15: siapa yang terbunuh](Victim-Characteristics-ms)
- [Langkah 16 hingga 19: tempat dan masa](Geography-and-Time-ms)
- [Jurnal tugasan](Journal-ms)
