[English](Racial-Demographics) · [Dansk](Racial-Demographics-da) · **Bahasa Malaysia**

# Langkah 7 dan 8: komposisi kaum dan kematian mengikut kaum

## Apa yang dilakukan langkah ini

Langkah 7 menunjukkan komposisi kaum setiap negeri sebagai carta palang bertindan, menggunakan bahagian banci yang dipuratakan merentas bandar dalam setiap negeri. Langkah 8 menunjukkan berapa ramai daripada 2,535 orang dalam pangkalan data Washington Post tergolong dalam setiap kaum, sebagai carta donat.

![Komposisi kaum setiap negeri](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-07-racial-makeup-by-state.png)

![Kematian mengikut kaum](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-08-deaths-by-race.png)

## Apa yang kami peroleh

- **Fahami apa yang diukur oleh sesuatu nombor.** Banci menganggap Hispanik sebagai etnik yang bertindih dengan kumpulan kaum, jadi lima bahagian sesebuah negeri boleh berjumlah lebih daripada 100 %. Palang bertindan itu naik melebihi 100 bagi sesetengah negeri, iaitu sifat data dan bukan pepijat.
- **Purata bandar bukan bahagian penduduk.** Bandar tidak ditimbang mengikut penduduk. Iowa (96.7 % kulit putih) dan Hawaii (33.4 % kulit putih) berada di dua hujung.
- **Bilangan bukan kadar.** Orang kulit putih ialah 47.4 % daripada yang terbunuh (1,201), kulit hitam 24.4 % (618) dan Hispanik 16.7 % (423). Kaum tidak diketahui bagi 7.7 % (195). Ini bahagian daripada satu bilangan; ia tidak menunjukkan sejauh mana mungkin seseorang daripada kaum tertentu terbunuh, kerana saiz kumpulan berbeza.
- **Tunjukkan data yang hilang.** Hirisan *Tidak diketahui* kekal kelihatan dan tidak dibuang.
- **Carta donat memerlukan sedikit hirisan.** Ia sesuai untuk tujuh kategori dan legenda memastikan hirisan kecil mudah dibaca.

## Di mana kodnya

`racial_makeup_by_state` dan `deaths_by_race` dalam `fatal_force.infrastructure.aggregation`; `stacked_bar_chart` dan `donut_chart` dalam `fatal_force.presentation.charts`.
