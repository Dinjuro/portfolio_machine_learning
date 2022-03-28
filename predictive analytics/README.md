# Laporan Proyek Machine Learning - Addina Dwi Nugroho

## Domain Proyek

Pada zaman sekarang, di zaman yang serba cepat, mobilisasi adalah hal yang tak terhindarkan. Oleh dari itu, tentunya kita membutuhkan alat transportasi untuk mempermudah terjadinya mobilisasi atau perpindahan dari tempat satu ke tempat lain. Salah satu alat transportasi yang umum digunakan adalah mobil. Alasannya, karena mobil cukup nyaman digunakan dan bisa melindungi pengguna dari panas dan hujan. Namun masalahnya, tidak semua orang mampu untuk membeli mobil baru guna menunjang mobilitasnya. Oleh karena itu, membeli mobil bekas adalah solusi yang tepat untuk mengatasi masalah tersebut.

## Business Understanding

Untuk membeli dan memilih mobil bekas, tentunya tidak semudah membeli mobil baru karena ada banyak hal yang perlu diperhatikan. Salah satunya adalah harga jual dari mobil bekas tersebut.

### Problem Statements

- Bagaimana korelasi antar fitur dapat mempengaruhi harga dari mobil bekas?
- Bagaimana membangun model dengan performa baik untuk memprediksi harga mobil bekas?

### Goals
- Dapat memahami korelasi antar fitur dapat mempengaruhi harga dari mobil bekas
- Dapat membangun model dengan performa baik untuk memprediksi harga mobil bekas

## Data Understanding
Untuk keperluan membuat aplikasi, kita memerlukan dataset yang akan kita gunakan untuk input data pada model yang nanti akan dibuat dan dilatih. Saya menggunakan dataset dari: [100,000 UK Used Car Data set](https://www.kaggle.com/adityadesai13/used-car-dataset-ford-and-mercedes?select=toyota.csv).

![Screenshot (21)](https://user-images.githubusercontent.com/93503149/146472182-f36f660e-acec-459a-9a0d-7f2ce2d1d183.png)


Dataset tersebut terdiri dari 10781 baris (records) dan 9 kolom (varabel) yaitu sebagai berikut:
- 3 variabel dengan tipe object, yaitu: model, transmission, dan fuelType. Kolom ini merupakan categorical features (fitur non-numerik).
- 5 variabel numerik dengan tipe data float64 dan int64 yaitu: year, mileage, tax, mpg, engineSize.
- 1 variabel numerik dengan tipe data int64, yaitu: price. Kolom ini merupakan target fitur.

### Penjalasan variabel-variabel pada dataset adalah sebagai berikut:
- model : merupakan jenis atau tipe mobil
- year  : merupakan tahun pembuatan mobil
- price : merupakan harga mobil
- transmission : merupakan jenis transmisi yang digunakan pada mobil
- mileage : merupakan jarak tempuh yang sudah dilalui mobil
- fuelType : merupakan jenis bahan bakar yang digunakan mobil
- tax : merupakan pajak mobil
- mpg : merupakan konsumsi bahan bakar mobil
- engineSize : merupakan ukuran mesin mobil

### Analisis Univariate
Untuk memahami data lebih dalam, dilakukan juga eksplorasi data dengan analisis univariate dan multivariate pada dataset. Analisis univariate dilakukan untuk menganalisis data terhadap satu variabel secara mandiri, tiap variabel dianalisis tanpa dikaitkan dengan variabel lainnya.

![Screenshot (25)](https://user-images.githubusercontent.com/93503149/146472613-4e06c7d2-39f4-4f3b-b98f-f976d4e7080d.png)

Dari grafik dapat disimpulkan bahwa jenis mobil terbanyak dalam dataset adalah seri 3 dan yg paling sedikit adalah X5

![Screenshot (27)](https://user-images.githubusercontent.com/93503149/146472732-7f4a09bc-99a1-4af0-a51b-1a94c6ccd6e3.png)

Lebih dari 50% mobil dalam dataset bertransmisi semi otomatis dan sisanya otomatis serta manual adalah yang paling sedikit

![Screenshot (29)](https://user-images.githubusercontent.com/93503149/146472806-9b963430-8e6e-47b4-9368-592a69555fc6.png)

Hampir 70% mobil berbahan bakar diesel, dan sisanya bensin serta hanya ada 1% mobil yang bermesin hybrid

![Screenshot (31)](https://user-images.githubusercontent.com/93503149/146473017-8ba0897d-328b-4344-8318-014d2dfe1a0c.png)

- Sebagian besar mobil dibuat pada tahun 2019
- Jarak tempuh mobil berbanding terbalik dengan jumlah mobil
- Sebagian besar mobil memiliki konsumsi bbm di bawah 200mpg
- Sebagian besar mobil memiliki harga antara 20000 sampai 30000
- hanya ada 1 nilai tax dan engineSize

### Analisis Multivariate
Analisis multivariate dilakukan untuk menunjukkan hubungan antar dua variabel atau lebih.

![Screenshot (33)](https://user-images.githubusercontent.com/93503149/146473125-dad4ba0c-83eb-41f5-bf4a-71a30aaa19e9.png)

- Mobil seri 6 memiliki harga termahal dann yang termurah adalah seri 1
- Harga mobil bertransmisi otomatis dan semi otomatis hampir sama, dan yang termurah adalah transmisi manual
- Harga mobil berbahan bakar diesel dan bensin hampir sama, dan yang paling mahal adalah mobil hybrid

![Screenshot (40)_LI](https://user-images.githubusercontent.com/93503149/146501767-7642d0c8-2e76-4fcd-92b8-7b12a0e6929b.jpg)

![Screenshot (39)](https://user-images.githubusercontent.com/93503149/146501579-b2dd8184-b583-4409-b433-c88709ca5087.png)


Pada kasus ini, kita akan melihat relasi antara semua fitur numerik dengan fitur target kita yaitu ‘price’. Untuk membacanya, perhatikan fitur pada sumbu y, temukan fitur target ‘price’, dan lihatlah grafik relasi antara semua fitur pada sumbu x dengan fitur price pada sumbu y. Dalam hal ini, fitur ‘price’ berada pada baris kedua (dari atas) sumbu y (ditandai oleh kotak merah). Sehingga, kita cukup melihat relasi antar fitur numerik dengan fitur target ‘price’ pada baris tersebut saja. 

- Pada fitur year, data memiliki korelasi positif. Artinya, semakin baru tahun pembuatan sebuah mobil, harganya juga semakin tinggi.
- pada fitur mileage, data memiliki korelasi negatif. Artinya, semakin jauh jarak yang telah ditempuh sebuah mobil, harganya juga semakin turun.
- Pada fitur mpg, korelasi data menunjukkan pola acak. Artinya, fitur tidak memiliki pengaruh terhadap harga mobil
- Pada fitur tax dan engineSize, hanya ada satu value. Sehingga tidak ada korelasi (tidak berpengaruh apapun) terhadap harga mobil

Dari beberapa poin di atas, dapat disimpulkan bahwa fitur yang paling berpengaruh terhadap harga mobil adalah fitur 'year' dan 'mileage'. Sedangan fitur 'mpg', 'tax', dan 'engineSize' tidak memiliki pengaruh terhadap harga mobil.

## Data Preparation

### Handling Missing Value
Sebelum data dilatih oleh model, data harus disiapkan terlebih dahulu. Hal pertama yang perlu dilakukan adalah memeriksa apakah ada missing value pada dataset. Jika ada, maka perlu dilakukan penangan missing value yang ada pada dataset. Pada proyek kali ini, dilakukan penghapusan pada variabel yang memiliki missing value karena data yang memiliki missing value cukup sedikit.

### Handling Outliers
Outliers adalah sampel yang nilainya sangat jauh dari cakupan umum data utama. Ia adalah hasil pengamatan yang kemunculannya sangat jarang dan berbeda dari data hasil pengamatan lainnya. Pada proyek ini, outliers dideteksi dengan teknik visualisasi data (boxplot). Sekarang, kita visualisasikan data dengan boxplot untuk mendeteksi outliers pada beberapa fitur numerik.

![Screenshot (45)](https://user-images.githubusercontent.com/93503149/146504193-492b347d-cafb-418b-9bf4-67666e14fd4c.png)

![Screenshot (47)](https://user-images.githubusercontent.com/93503149/146504317-5b189ffe-ec9c-44d0-9239-8c252542e914.png)

![Screenshot (49)](https://user-images.githubusercontent.com/93503149/146504404-2523a8db-bd8a-46fd-9878-b3daa3fc60f8.png)

![Screenshot (51)](https://user-images.githubusercontent.com/93503149/146504527-99aaa70f-2ea8-44bc-b04b-0398165d4d66.png)

![Screenshot (53)](https://user-images.githubusercontent.com/93503149/146504642-bcc80637-8f13-4b9a-9ecc-052a2323f77f.png)

![Screenshot (55)](https://user-images.githubusercontent.com/93503149/146504731-49034db7-f101-49c5-8617-43d658b1b3d3.png)

Dari grafik, terlihat ada outliers pada fitur numerik di atas. Kemudian, penanganan outliers dilakukan dengan teknik IQR method. IQR digunakan untuk mengidentifikasi outlier yang berada di luar Q1 dan Q3. Nilai apa pun yang berada di luar batas ini dianggap sebagai outlier. 

Seltman dalam “Experimental Design and Analysis” [24] menyatakan bahwa outliers yang diidentifikasi oleh boxplot (disebut juga “boxplot outliers”) didefinisikan sebagai data yang nilainya 1.5 QR di atas Q3 atau 1.5 QR di bawah Q1.

Hal pertama yang perlu dilakukan adalah membuat batas bawah dan batas atas. Untuk membuat batas bawah, kurangi Q1 dengan 1,5 * IQR. Kemudian, untuk membuat batas atas, tambahkan 1.5 * IQR dengan Q3. 

![Screenshot (57)](https://user-images.githubusercontent.com/93503149/146504868-75fb2c2e-2e3f-4db1-8e03-c1ed9ad9c114.png)

Dataset sekarang telah bersih dan memiliki 3259 sampel.

### Encoding fitur kategori
Gunakan teknik Encoding untuk menyiapkan data sebelum dilatih model. Untuk melakukan proses encoding fitur kategori, salah satu teknik yang umum dilakukan adalah teknik one-hot-encoding. Library scikit-learn menyediakan fungsi ini untuk mendapatkan fitur baru yang sesuai sehingga dapat mewakili variabel kategori.

### Train-Test-Split
Dilakukan proses pembagian dataset menjadi dua. yaitu data training dan data testing. Karena jumlah data tidak terlalu banyak, ntuk proyek kali ini, pembagian dilakukan dengan persentase 80% untuk data training, dan 20% untuk data testing, sehingga data training terdiri dari 2601 sampel, dan data testing terdiri dari 651 sampel dari total 3252 sampel.

### Standardisasi
Pada tahap akhir data preparation dilakukan proses standardisasi untuk membuat fitur data menjadi bentuk yang lebih mudah diolah oleh algoritma model. Untuk proyek kali ini, teknik standardisasi yang digunakan adalah teknik StandarScaler dari library Scikitlearn. StandardScaler melakukan proses standarisasi fitur dengan mengurangkan mean (nilai rata-rata) kemudian membaginya dengan standar deviasi untuk menggeser distribusi.  StandardScaler menghasilkan distribusi dengan standar deviasi sama dengan 1 dan mean sama dengan 0. Sekitar 68% dari nilai akan berada di antara -1 dan 1.

## Modeling
Pada proyek ini, kita akan mengembangkan model machine learning dengan tiga algoritma. Ketiga algoritma yang akan kita gunakan, adalah :
- K-Nearest Neighbor

        Algoritma KNN menggunakan ‘kesamaan fitur’ untuk memprediksi nilai dari setiap data yang baru. Dengan kata lain, setiap data baru diberi nilai berdasarkan seberapa mirip titik tersebut dalam set pelatihan. Pada proyek ini,digunakan parameter n_neighbors=8 tetangga dan metric Euclidean untuk mengukur jarak antara titik. Pada tahap ini kita hanya melatih data training dan menyimpan data testing untuk tahap evaluasi.

- Random Forest
       
        Random forest pada dasarnya adalah versi bagging dari algoritma decision tree. Pada proyek kali ini, algoritma menggunakan parameter  n_estimators (jumlah pohon/trees) = 30.
- Boosting Algorithm

        Algoritma boosting bekerja dengan membangun model dari data latih. Kemudian ia membuat model kedua yang bertugas memperbaiki kesalahan dari model pertama. Model ditambahkan sampai data latih mencapai jumlah maksimum model untuk ditambahkan. Pada proyek kali ini, digunakan metode adaptive boosting AdaBoost dengan parameter  n_estimators (jumlah pohon/trees) = 30

## Evaluation
Metrik yang digunakan pada prediksi adalah MSE atau Mean Squared Error yang menghitung jumlah selisih kuadrat rata-rata nilai sebenarnya dengan nilai prediksi. MSE didefinisikan dalam persamaan berikut :

![mse](https://user-images.githubusercontent.com/93503149/146109704-0116acbb-cf3d-49f1-9ef3-f9058af836e1.jpeg)

Keterangan:

N = jumlah dataset

yi = nilai sebenarnya

y_pred = nilai prediksi

Evaluasi dilakukan dengan membandingan hasil MSE ketiga model kemudian memilih yang terkecil. Namun, sebelum MSE ketiga model dibandingkan, perlu dilakukan proses scaling terhadap data uji terlebih dahulu. Hal ini harus dilakukan agar skala antara data latih dan data uji sama dan evaluasi bisa dilakukan.

Untuk memudahkan evaluasi, dilakukan plot metrik dengan bar chart.

![evaluasi model](https://user-images.githubusercontent.com/93503149/146110718-4b919c5a-86dc-4470-a533-9b1598c348a0.png)

Dari visualisasi bar chat, disimpulkan bahwa model KNN memberikan nilai eror yang paling kecil. Model inilah yang dipilih sebagai model terbaik untuk melakukan prediksi harga mobil

**---Ini adalah bagian akhir laporan---**