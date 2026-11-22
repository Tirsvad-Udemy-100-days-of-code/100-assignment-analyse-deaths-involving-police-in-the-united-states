[English](Journal) · [Dansk](Journal-da) · **Bahasa Malaysia**

# Jurnal tugasan

Tugasan ini mengemukakan lima soalan. Berikut jawapan kami.

## Bagaimana kami menghampiri projek ini?

Kami merancang dahulu: kes perniagaan, pihak berkepentingan, tujuh batu tanda dan senarai tugas, setiap satu disemak sebelum sebarang kod. Kemudian setiap batu tanda mengikut langkah kuliah mengikut urutan: muat dan bersihkan data, kemudian satu carta bagi setiap langkah. Logik diletakkan dalam pakej kecil yang diuji, dan buku nota Jupyter hanya memanggilnya dan menunjukkan hasil. Setiap langkah menyimpan cartanya sebagai tangkapan skrin, dan setiap langkah mempunyai halaman wiki dalam tiga bahasa.

## Apa yang sukar?

- Fail data nampak mudah tetapi tidak: teks Windows-1252 dan satu *carriage return* sebagai pengakhir baris, pemegang tempat seperti `(X)` dan `250,000+` dalam lajur nombor, dan bahagian Hispanik yang bertindih dengan bahagian kaum.
- Topik yang sensitif. Carta bilangan mengundang pembacaan sebagai kadar atau sebab. Kami meletakkan had di sebelah setiap carta dan tidak menyerahkannya kepada pembaca.
- Memadankan bandar antara dua sumber: banci menulis "Los Angeles city", pangkalan data polis "Los Angeles".

## Apa yang mudah?

- Setelah fungsi pembersihan wujud, setiap carta ialah pengumpulan pendek dan fungsi lukisan.
- Ujian pada jadual kecil menangkap kesilapan awal, seperti kedudukan seri dalam peringkat dan bulan yang hilang dalam siri masa.

## Apa yang akan kami baiki lain kali?

- Tentukan kaedah tangkapan skrin sebelum carta pertama, supaya rajah kelihatan sama sejak awal.
- Timbang purata negeri mengikut penduduk bandar. Fail banci tiada lajur penduduk, jadi ini memerlukan sumber lain.
- Tambah kadar bagi setiap 100,000 orang, yang dibayangkan tugasan tetapi tidak dapat diberikan terus oleh fail yang dibekalkan.

## Apakah pembelajaran terbesar?

Membersihkan dan menyemak data memerlukan lebih teliti daripada melukisnya, dan carta hanya menjawab soalan yang dibina untuknya. Palang bilangan bukan kadar, korelasi bukan sebab, dan data yang hilang harus kekal kelihatan.

## Apa yang akan kami lakukan secara berbeza?

Bermula dengan kamus data (apa maksud setiap lajur dan nilai mana pemegang tempat) dan menulis ujian pembersihan daripadanya. Ini akan menemui pengakhir baris *carriage return* dan pemegang tempat nombor pada hari pertama.
