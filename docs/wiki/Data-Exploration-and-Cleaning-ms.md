[English](Data-Exploration-and-Cleaning) · [Dansk](Data-Exploration-and-Cleaning-da) · **Bahasa Malaysia**

# Langkah 1 dan 2: penerokaan dan pembersihan data

## Apa yang dilakukan langkah ini

Langkah 1 melihat data mentah: berapa baris dan lajur setiap satu daripada lima fail, berapa nilai yang hilang dan sama ada baris berulang. Langkah 2 membersihkan data supaya carta seterusnya berdasarkan nombor yang boleh dipercayai.

![Penerokaan data mentah](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-01-data-exploration.png)

![Data selepas pembersihan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-02-data-cleaning.png)

## Apa yang kami peroleh

- **Lihat sebelum melukis carta.** Fail kematian mempunyai 2535 baris dan 346 nilai yang hilang (umur 77, bangsa 195, melarikan diri 65, bersenjata 9) dan tiada id berganda. Setiap fail banci mempunyai kira-kira 29 000 baris bandar.
- **Fail sebenar tidak kemas.** Fail CSV menggunakan teks Windows-1252 dan satu *carriage return* sebagai pengakhir baris, jadi pembacaan biasa gagal. Satu fungsi pembaca kecil kini menyembunyikannya.
- **Pemegang tempat bukan nombor.** Nilai seperti `(X)`, `-` dan `250,000+` ditukar kepada nilai yang hilang atau nombor biasa. Nilai banci yang hilang kekal hilang dan bukan menjadi sifar, kerana sifar akan menurunkan purata.
- **Ujian memastikan pembersihan jujur.** Fungsi pembersihan mempunyai ujian unit pada fail kecil, jadi perubahan yang merosakkannya dikesan serta-merta.
- **Satu tangkapan skrin bagi setiap langkah** disimpan oleh kod dalam `docs/screenshots/`, supaya boleh dijana semula.

## Di mana kodnya

`fatal_force.infrastructure.csv_reader`, `exploration` dan `cleaning`; pembantu rajah ialah `fatal_force.presentation.screenshots`.
