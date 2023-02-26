# Tugas Kecil 2 Mata Kuliah Strategi Algoritma 
## Mencari Pasangan Titik Terdekat 3D dengan Algoritma Divide and Conquer

### Deskripsi
Program ini dikembangkan dari algoritma pencarian pasangan titik dengan jarak terdekat pada bidang datar (2D). Program dapat mencari pasangan titik dengan jarak terdekat pada bidang 3D hingga N Dimensi. Paradigma algoritma yang digunakan pada pembuatan program ini adalah Divide and Conquer, yaitu algoritma dengan membagi sebuah persoalan menjadi beberapa upa persoalan yang memiliki kemiripan dengan persoalan semula dengan ukuran yang lebih kecil sehingga persoalan menjadi lebih kecil dan komputasi lebih sedikit.

### Pendekatan Algoritma Divide and Conquer
1. Program memperoleh n, yaitu banyak titik, dan dimensi da pengguna
2.	Dari banyak titik dan dimensi yang diperoleh, program menentukan secara random posisi titik-titik tersebut dengan batasan -1000 hingga 1000 untuk setiap sumbunya dan disimpan dalam sebuah matriks dengan baris sebagai titik dan kolom sebagai dimensi dan diurutkan dengan algoritma quicksort berdasarkan sumbu x.
3.	Matriks tersebut kemudian dipecah menjadi 2 upa matriks dengan ukuran yang kurang lebih sama
4.	Pemecahan tersebut terus dilakukan hingga pada sebuah matriks hanya terdapat 2 atau 3 titik saja
5.	Ketika sudah terdapat 2 titik, jarak terdekat adalah jarak Euclidean antara 2 titik tersebut. Jika terdapat 3 titik, hitung jarak antara semua titik tersebut menggunakan rumus Euclidean dan tentukan yang paling kecil
6.	Jarak terkecil yang telah diperoleh tersebut kemudian dibandingkan dengan upa matriks yang lain terus hingga kembali ke matriks utama dan ditentukan jarak terkecilnya. 
7.	Karena terdapat kemungkinan terdapat pasangan titik yang jaraknya lebih kecil terdapat diantara pembagian tersebut, lakukan pencarian antara semua titik yang memiliki jarak lebih kecil dari jarak terkecil sebelumnya tersebut pada semua sumbu. Jika ada, maka pasangan titik tersebut menjadi pasangan titik dengan jarak terkecil dan hitung jaraknya
8.	Lakukan perbandingan antara jarak yang diperoleh pada nomor 6 dan 7 dan tentukan jarak terkecil dan pasangan titiknya
9.	Lakukan pencarian jarak terdekat dengan algoritma Brute Force
10.	Jarak, titik 1, titik 2, banyak perhitungan Euclidean, dan waktu komputasi dengan Divide and Conquer dan Brute Force ditampilkan

### Keperluan
1. Instalasi Matplotlib
2. Instalasi Tkinter

### Deskripsi *Directory*
1. folder bin <br>
berisikan *file* txt (mengarahkan untuk *run* dari main.py)
2. folder doc <br>
berisikan *file* laporan
3. folder src <br>
berisikan *file source code*

### Memulai program
Untuk memulai program, *run file* main.py pada folder src

### Pembuat
Hosea Nathanael Abetnego - 13521057
