[English](Poverty-and-Graduation) · [Dansk](Poverty-and-Graduation-da) · **Bahasa Malaysia**

# Langkah 3 hingga 6: kemiskinan dan tamat sekolah menengah

## Apa yang dilakukan langkah ini

Fail banci menyenaraikan beribu-ribu bandar. Langkah 3 dan 4 mengambil purata nilai bandar bagi setiap negeri dan menyusun 51 negeri (50 negeri dan DC) mengikut kadar kemiskinan dan kadar tamat sekolah menengah. Langkah 5 dan 6 meletakkan kedua-dua ukuran bersebelahan: carta garis dengan dua paksi-y dan plot serakan dengan garis regresi.

![Kadar kemiskinan mengikut negeri](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-03-poverty-rate.png)

![Kadar tamat sekolah menengah mengikut negeri](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-04-graduation-rate.png)

![Kemiskinan dan tamat sekolah sebagai garis](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-05-poverty-and-graduation-lines.png)

![Plot serakan dengan garis regresi](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-06-poverty-vs-graduation-scatter.png)

## Apa yang kami peroleh

- **Gabungkan dahulu, kemudian susun.** Mississippi mempunyai purata kadar kemiskinan tertinggi (26.9 %) dan New Jersey terendah (8.2 %). Texas mempunyai kadar tamat sekolah terendah (75.7 %) dan Massachusetts tertinggi (92.4 %).
- **Carta garis alat yang salah di sini.** Negeri tiada susunan semula jadi, jadi kedua-dua garis kebanyakannya menunjukkan hingar. Plot serakan menunjukkan hubungan jauh lebih baik: r Pearson ialah -0.86 dan garis padanan menurun 0.83 mata peratus kadar tamat sekolah bagi setiap mata kemiskinan tambahan.
- **Korelasi bukan sebab.** Kedua-dua ukuran bergerak bersama, tetapi data tidak boleh mengatakan kemiskinan menyebabkan kadar tamat lebih rendah, atau sebaliknya. Kedua-duanya mungkin disebabkan faktor lain.
- **Pilih carta mengikut soalan.** Palang tersusun menjawab "siapa tertinggi", plot serakan menjawab "adakah ia bergerak bersama".
- **Fungsi tulen yang kecil mudah diuji.** Purata mengikut negeri, penggabungan dan padanan garis masing-masing mempunyai ujian unit pada jadual kecil.

## Di mana kodnya

`fatal_force.infrastructure.aggregation`, `fatal_force.domain.regression` dan `fatal_force.presentation.charts`.
