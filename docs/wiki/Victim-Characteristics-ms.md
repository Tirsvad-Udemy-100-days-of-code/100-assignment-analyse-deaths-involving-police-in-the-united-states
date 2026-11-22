[English](Victim-Characteristics) · [Dansk](Victim-Characteristics-da) · **Bahasa Malaysia**

# Langkah 9 hingga 15: siapa yang terbunuh

## Apa yang dilakukan langkah ini

Langkah ini menerangkan 2,535 orang dalam pangkalan data Washington Post: jantina, umur, cara kematian, sama ada mereka bersenjata, umur mengikut kaum, tanda penyakit mental, tahap ancaman dan sama ada mereka melarikan diri.

![Kematian mengikut jantina](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-09-deaths-by-gender.png)

![Taburan umur](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-10-age-distribution.png)

![Umur mengikut cara kematian](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-11-age-by-manner-of-death.png)

![Bersenjata dan tidak bersenjata](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-12-armed-and-unarmed.png)

![Umur mengikut kaum](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-13-age-by-race.png)

![Penyakit mental](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-14-mental-illness.png)

![Tahap ancaman dan melarikan diri](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/100-assignment-analyse-deaths-involving-police-in-the-united-states/raw/branch/main/docs/screenshots/step-15-threat-and-fleeing.png)

## Apa yang kami peroleh

- **Kebanyakan yang terbunuh ialah lelaki.** 2,428 (95.8 %) lelaki dan 107 (4.2 %) wanita. Cara kematian ialah *shot* bagi 2,363 dan *shot and Tasered* bagi 172.
- **Umur.** Umur median ialah 34 (2,458 umur diketahui) dan 18.3 % daripada yang diketahui umurnya berumur bawah 25. Histogram dengan garis KDE menunjukkan bentuknya; plot kotak membandingkan kumpulan.
- **Bersenjata tidak bermaksud satu perkara.** 92.9 % direkodkan bersenjata, 6.7 % (171) tidak bersenjata dan 0.4 % tidak diketahui. Kumpulan bersenjata termasuk *undetermined* (117) dan *toy weapon* (104), jadi angka utama bergantung pada takrifan. Pistol ialah senjata paling biasa (1,398).
- **Taburan mengikut kumpulan.** Garis ketumpatan setiap kaum memuncak pada umur berbeza (kulit hitam dan Hispanik sekitar 25, kulit putih sekitar 33), tetapi kumpulan kecil memberi garis kasar, jadi legenda menunjukkan saiz kumpulan.
- **Konteks penting.** 25.0 % rekod mencatat tanda penyakit mental. Tahap ancaman ialah *attack* bagi 1,611, *other* bagi 766 dan *undetermined* bagi 158; 1,695 tidak melarikan diri.
- **Tulis KDE sendiri.** Anggaran ketumpatan kernel Gauss dengan lebar jalur Silverman memerlukan kira-kira dua puluh baris Python standard dan tiada pustaka tambahan; ia mempunyai ujian sendiri.

## Di mana kodnya

`fatal_force.infrastructure.victims`, `fatal_force.domain.kde` dan `armed`, `fatal_force.presentation.charts` dan `distributions`.
