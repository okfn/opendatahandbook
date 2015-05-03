---
section: guide
lang: id
title: Format File
---

## Sebuah Tinjauan Format File

### JSON

JSON adalah format file sederhana yang sangat mudah bagi setiap bahasa pemrograman untuk membacanya. Kesederhanaannya mempunyai arti bahwa secara umum memudahkan komputer untuk memprosesnya dibandingkan yang lain, seperti XML.

### XML

XML adalah format yang digunakan secara luas untuk pertukaran data karena memberikan peluang yang baik untuk menjaga struktur dalam data dan file cara yang dibangun pada, dan memungkinkan pengembang untuk menulis bagian dari dokumentasi dengan data tanpa mengganggu pembacaan mereka.

### RDF

Sebuah format W3C-yang direkomendasikan disebut RDF memungkinkan untuk mewakili data dalam bentuk yang membuatnya lebih mudah untuk menggabungkan data dari berbagai sumber. Data RDF dapat disimpan dalam XML dan JSON, antara serialisasi lainnya. RDF mendorong penggunaan URL sebagai pengidentifikasi, yang menyediakan cara mudah untuk interkoneksi secara langsung dengan inisiatif {term:data terbuka} yang telah ada di web. RDF masih belum secara luas digunakan, tetapi telah menjadi tren di kalangan inisiatif Pemerintah Terbuka, termasuk proyek Data Terbuka Tertaut Pemerintah Inggris dan Spanyol. Sang penemu web, Tim Berners-Lee, baru-baru ini mengusulkan [fivesstar](http://lab.linkeddata.deri.ie/2010/star-scheme-by-example/) scheme yang mencakup data RDF terkait sebagai tujuan yang harus dicapai bagi inisiatif data terbuka.

### Spreadsheet

Banyak yang berwenang mempunyai informasi disimpan dalam spreadsheet. sebagai contoh Microsoft Excel. Data ini sering dapat digunakan langsung dengan deskripsi yang benar dari apa yang kolom yang berbeda berarti.

Bagaimanapun juga, dalam beberapa kasus bisa berupa macro dan formula pada spreadsheet, yang mungkin lebih rumit untuk menangani. Oleh karena itu, disarankan untuk mendokumentasikan setiap perhitungan di samping menggunakan spreadsheet, karena pada umumnya lebih mudah diakses pengguna dalam membacanya.

### File Dipisahkan Koma

File CSV dapat menjadi format yang sangat berguna karena ringan dan dengan demikian cocok untuk mentransfer kumpulan data yang besar dengan struktur yang sama. Namun, format ini sangat sederhana hingga sering menjadi tidak berguna bila tanpa dokumentasi karena hampir mustahil untuk menebak makna dari kolom yang berbeda. Oleh karena itu sangat penting bagi format dengan tanda pemisah koma dilengkapi pula dengan dokumentasi masing-masing field secara akurat.

Selanjutnya adalah penting bagi struktur file untuk dihargai, sebuah kelalaian pada sebuah field dapat mengganggu pembacaan semua data yang tersisa di dalam file tanpa adanya kesempatan untuk memperbaikinya, karena tidak dapat ditentukan bagaimana data yang tersisa harus diinterpretasikan.

### Dokumen Teks

Dokumen klasik dalam format seperti Word, ODF, OOXML, atau PDF mungkin cukup untuk menunjukkan jenis data tertentu - misalnya, mailing list-mailing list yang relatif stabil atau yang serupa. Mungkin akan murah untuk menampilkan dengan format tersebut, sebagaimana seseringnya data-data tersebut lebih banyak dihasilkan dengan format tersebut. Format tersebut tidak memberikan dukungan untuk menjaga struktur tetap konsisten, yang berarti sulit untuk memasukkan data secara otomatis. Pastikan untuk menggunakan template sebagai dasar dokumen yang akan menampilkan data untuk digunakan kembali, sehingga setidaknya memungkinkan untuk menarik informasi dari dokumen tersebut.

Hal ini juga dapat mendukung penggunaan lebih lanjut dari data yang menggunakan tanda kode tipografi sebanyak mungkin sehingga menjadi lebih mudah untuk mesin untuk membedakan judul (jenis apa pun ditentukan) dari konten dan sebagainya. Umumnya dianjurkan untuk tidak ditampilkan dalam format pengolah kata, jika data ada dalam format yang berbeda.

### Plain Text

Dokumen teks biasa (.txt) sangat mudah dibaca komputer. Mereka pada umumnya mengesampingkan struktur metadata dalam dokumen. Namun hal ini menuntut pengembang untuk membuat parser yang dapat menafsirkan setiap dokumen sebagaimana yang tampil.

Beberapa masalah dapat disebabkan oleh peralihan file plain text antar sistem operasi. MS Windows, Mac OS X dan varian Unix lainnya memiliki cara tersendiri untuk memberitahu komputer bahwa mereka telah mencapai akhir baris dari file.

### Gambar terpindai

Mungkin hal tersebut merupakan bentuk yang setidaknya sesuai untuk kebanyakan data, namun TIFF dan JPEG-2000 keduanya setidaknya bisa menandai mereka dengan dokumentasi apa yang ada dalam gambar - hingga untuk menandai sebuah gambar dokumen dengan konten teks lengkap dari dokumen. Ini mungkin relevan untuk menampilkan data mereka sebagai gambar yang datanya tidak dibuat secara elektronik - sebuah contoh nyata adalah catatan-catatan gereja tua dan bahan-bahan arsip lainnya - dan sebuah gambar lebih baik daripada tidak sama sekali.

### Format hak milik

Beberapa sistem terdedikasi, dll. mempunyai format data mereka sendiri yang dapat menyimpan dan mengekspor data yang masuk di dalamnya. Terkadang cukup mengekspos data dengan format demikian - terutama jika ke depannya berencana untuk penggunaan kembali sistem yang sama sebagaimana sebelumnya. Di mana selanjutnya informasi dengan format hak milik ini dapat ditemukan harus selalu dapat ditunjukkan, misalnya dengan memberikan tautan ke situs penyedia. Umumnya dianjurkan untuk menampilkan data dalam format non-hak milik di mana hal itu lebih layak.

### HTML

Saat ini data sudah banyak tersedia dalam format HTML di berbagai situs. Format HTML ini mungkin akan mencukupi jika data tersebut sudah sangat stabil dan dalam lingkup terbatas. Dalam beberapa kasus, dapat menjadi lebih baik untuk memiliki data dalam bentuk yang mudah untuk diunduh dan mudah dimanipulasi, tapi karena saat ini sudah semakin murah dan mudah untuk merujuk ke suatu halaman pada situs web, maka format HTML bisa menjadi titik awal yang baik dalam menampilkan data.

Biasanya, akan sangat tepat untuk menggunakan tabel dalam dokumen HTML untuk menyimpan data, serta menjadi hal yang penting pula untuk menampilkan field data yang beragam dan masing-masing diberikan ID dapat membuatnya mudah untuk menemukan dan memanipulasi data. Yahoo telah mengembangkan sebuah perangkat (<http://developer.yahoo.com/yql/>) yang dapat mengekstrak informasi terstruktur dari sebuah situs web, dan bahkan perangkat seperti itu dapat melakukan lebih banyak lagi dengan data jika ditandai dengan seksama.

## Format File Terbuka

Sekalipun bila informasi disediakan secara elektronik, format yang bisa dibaca mesin, dan dalam rinciannya, munkin terdapat beberapa isu berkaitan dengan format file-nya.

Format di mana informasi diterbitkan - dengan kata lain, basis digital tempat informasi disimpan - dapat pula menjadi "terbuka" atau "tertutup". Format terbuka adalah salah satu di mana spesifikasi untuk perangkat lunak tersedia untuk siapapun, gratis, sehingga siapa pun dapat menggunakan spesifikasi perangkat lunak mereka sendiri tanpa ada pembatasan pada re-gunakan dikenakan oleh hak kekayaan intelektual.

Jika format sebuah file "tertutup", ini kemungkinan karena file tersebut dibuat dalam format hak milik dan spesifikasinya tidak tersedia untuk umum, atau bisa pula karena file tersebut dalam format hak milik sekalipun spesifikasinya telah dibuat publik, penggunaannya kembali pun terbatas. Jika informasi dirilis dalam format file tertutup, hal ini dapat menyebabkan hambatan yang signifikan saat menggunakan kembali informasi yang dikodekan di dalamnya, serta memaksa orang-orang yang ingin menggunakan informasi tersebut untuk membeli perangkat lunak yang diperlukan.

Keuntungan dari format file terbuka adalah mereka memperkenankan para pengembang untuk membuat multi paket perangkat lunak dan layanan yang menggunakan format ini. Hal ini meminimalisir kendala dalam mengunakan ulang informasi yang dimilikinya.

Menggunakan file berformat hak milik yang spesifikasinya tidak tersedia untuk umum dapat menciptakan ketergantungan pada perangkat lunak pihak ketiga atau pemegang lisensi format file tersebut. Dalam skenario terburuk, ini dapat berarti informasi hanya dapat dibaca dengan menggunakan paket perangkat lunak tertentu, yang bisa saja mahal, atau mungkin sudah usang.

Hal yang menarik dan menguntungkan dari perspektif {term:data terbuka pemerintah} adalah bahwa setiap informasi dirilis dalam **format file terbuka yang dapat dibaca oleh mesin.**

### Contoh: Data lalulintas UK

Andrew Nicolson adalah seorang pengembang perangkat lunak yang terlibat dalam sebuah (sangat sukses) kampanye menentang pembangunan jalan bebas hambatan Westbury Eastern di Inggris. Andrew telah tertarik dengan mengakses dan menggunakan data lalulintas jalan yang digunakannya untuk memperkuat usulannya. Ia berupaya mendapatkan sejumlah data relevan melalui kebebasan dalam mendapatkan informasi, tetapi pemerintah lokal menyediakan datanya dalam format hak milik yang hanya bisa dibaca menggunakan perangkat lunak yang dibuat oleh Saturn, sebuah perusahaan yang khusus bergerak dalam pemodelan dan prediksi lalulintas. Masalahnya tidak ada ketentuan yang dapat menyediakan versi "hanya baca" dari perangkat lunak tersebut, sehingga kelompok Andrew tidak punya pilihan selain membeli lisensi perangkat lunak tersebut dengan harga £500 (€600) itupun dengan potongan untuk versi edukasi. Paket utama perangkat lunak tersebut hingga April 2010 harga yang ditawarkan Saturn berkisar antara £13,000 (hingga lebih dari €15,000), sebuah harga yang tidak akan terjangkau oleh kebanyakan warga masyarakat biasa.

Meskipun tidak ada akses ke informasi, hukum memberi hak untuk mengakses informasi dalam format terbuka, setiap inisiatif data terbuka pemerintah perlu dimulai dengan didampingi dokumen-dokumen kebijakan yang menyatakan informasi resmi harus tersedia dalam format file terbuka. Pengaturan standar emas telah menjadi agenda kerja Obama melalui Ketentuan Terbuka Pemerintah yang diterbitkan pada Desember 2009 yang mengatakan:

> *Untuk tujuan praktis dan tunduk pada pembatasan yang valid, lembaga-lembaga harus mempublikasikan informasi secara daring dalam format terbuka yang dapat diambil, diunduh, diindeks, dan dicari oleh aplikasi web yang umum digunakan dalam pencarian. Format terbuka adalah salah satu platform yang independen, dapat dibaca mesin, dan dibuat tersedia untuk umum tanpa pembatasan yang akan menghambat penggunaan kembali informasi tersebut.*

## Bagaimana saya bisa menggunakan format yang diberikan?

Ketika pihak otoritas harus menunjukkan data baru - data yang belum dipamerkan sebelumnya - anda harus memilih format yang dapat memberikan keseimbangan terbaik antara biaya dan kesesuaian dengan tujuan. Untuk setiap formatnya ada beberapa hal yang harus anda sadari, dan bagian ini bertujuan untuk menjelaskannya.

Bagian ini hanya berfokus pada bagaimana memotong permukaan menjadi cara pengaturan terbaik sehingga mesin dapat mengaksesnya secara langsung. Nasihat dan bimbingan tentang bagaimana situs dan solusi web harus didesain agar dapat ditemukan dari tempat lain.

### Layanan web

Untuk data yang berubah secara berkala, dan ketika untuk mendapatkannya telah dibatasi jumlahnya, menjadi sangat relevan untuk mengekspos data melalui layanan web. Terdapat beberapa cara untuk membuat layanan web, tetapi beberapa di antaranya yang paling sering digunakan adalah SOAP dan REST. Umumnya, SOAP melampaui REST, namun layanan REST lebih mudah untuk dikembangkan dan digunakan, sehingga ia menjadi standar yang banyak digunakan.

### Basisdata

Seperti layanan web, basisdata menyediakan akses langsung ke data secara dinamis. Basisdata mempunyai kelebihan yaitu di mana para penggunanya bisa menyimpan secara bersama hanya dengan mengekstrasi apa yang mereka butuhkan.

Terdapat beberapa masalah keamanan mengenai fasilitas ekstrasi basisdata dengan kendali jarak jauh dan akses basisdata hanya akan berguna bila strukturnya dan kebernilaian dari tabel-tabel individualnya dan field-field telah didokumentasikan dengan baik. Seringkali, adalah hal yang relatif sederhana dan murah untuk membuat layanan web yang mengekspos data dari basisdata, yang dapat menjadi cara mudah untuk mengatasi masalah keamanan.