[English](Geography-and-Time) · [Dansk](Geography-and-Time-da) · **Bahasa Malaysia**

# Langkah 16 hingga 19: tempat dan masa

## Apa yang dilakukan langkah ini

Langkah 16 menyusun sepuluh bandar dengan pembunuhan paling banyak. Langkah 17 membandingkan, bagi bandar itu, bahagian setiap kaum dalam kalangan yang terbunuh dengan bahagian bancinya. Langkah 18 melukis pembunuhan bagi setiap negeri pada peta. Langkah 19 mengikuti bilangan pembunuhan bulan demi bulan.

![Sepuluh bandar teratas](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-16-top-cities.png)

![Nisbah mengikut kaum di sepuluh bandar](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-17-rate-by-race-top-cities.png)

![Peta pembunuhan mengikut negeri](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-18-deaths-by-state-map.png)

![Pembunuhan mengikut masa](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-19-deaths-over-time.png)

## Apa yang kami peroleh

- **Bilangan mengikut saiz.** Los Angeles (39), Phoenix (31), Houston (26) dan Chicago (25) mendahului bandar; California (424), Texas (225) dan Florida (154) mendahului negeri. Ini tempat terbesar, jadi bilangan sahaja tidak menunjukkan di mana seseorang menghadapi risiko lebih tinggi.
- **Padankan nama sebelum menggabung.** Banci menulis "Los Angeles city" dan pangkalan data polis "Los Angeles". Fungsi yang menormalkan nama memadankan 1,295 daripada 1,534 bandar yang ada kematian.
- **Bandingkan bahagian dengan berhati-hati.** Di sepuluh bandar, bahagian orang kulit hitam dalam kalangan yang terbunuh ialah 1.1 hingga 2.9 kali bahagian mereka di bandar, dan kulit putih 0.17 hingga 1.0 kali. Setiap bandar hanya ada 15 hingga 39 pembunuhan, kumpulan tanpa pembunuhan menunjukkan 0, dan bahagian Hispanik banci bertindih dengan bahagian kaum, jadi palang tunggal agak kasar.
- **Peta koroplet memerlukan eksport statik.** plotly melukis peta interaktif; tangkapan skrin memerlukan pakej `kaleido`, sebab itu ia berada dalam tambahan pilihan `analysis`.
- **Ketahui julat masa.** Fail meliputi Januari 2015 hingga Julai 2017 (31 bulan, 991 pembunuhan pada 2015, 963 pada 2016 dan 581 pada 2017 yang tidak lengkap). Garis aliran lurus hampir mendatar (-0.04 sebulan), dan min bergolek melicinkan hingar bulanan.

## Di mana kodnya

`fatal_force.infrastructure.geography` dan `timeline`, `fatal_force.presentation.charts` dan `maps`.
