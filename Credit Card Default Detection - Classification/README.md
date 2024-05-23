[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/k5VWQSvJ)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14831379&assignment_repo_type=AssignmentRepo)
# Graded Challenge 5 - Set 1

*Graded Challenge ini dibuat guna mengevaluasi pembelajaran pada Hacktiv8 Data Science Fulltime Program khususnya pada konsep Classification terutama Logistic Regression, SVM, dan KNN*

---

## Assignment Objectives

*Graded Challenge 5* ini dibuat guna mengevaluasi konsep Logistic Regression, SVM, dan KNN sebagai berikut:

- Mampu memperoleh data menggunakan BigQuery.

- Mampu memahami konsep Classification dengan Logistic Regression, SVM, dan KNN.

- Mampu mempersiapkan data untuk digunakan dalam model Logistic Regression, SVM, dan KNN.

- Mampu mengimplementasikan Logistic Regression, SVM, dan KNN untuk membuat prediksi.

---

## Dataset

```{attention}
Perhatikan petunjuk penggunaan dataset!
```

1. Buka [Google Cloud Platform](https://console.cloud.google.com/), masuk ke BigQuery, lalu buka tab `bigquery-public-data` atau link [berikut](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=ml_datasets&t=credit_card_default&page=table) untuk langsung menuju ke dataset.

2. Gunakan dataset `ml_datasets` dari database bernama `credit_card_default`.

3. Buatlah query dengan kriteria sebagai berikut:
   - Pilih **HANYA** kolom `limit_balance, sex, education_level, marital_status, age, pay_0, pay_2, pay_3, pay_4, pay_5, pay_6, bill_amt_1, bill_amt_2, bill_amt_3, bill_amt_4, bill_amt_5, bill_amt_6, pay_amt_1, pay_amt_2, pay_amt_3, pay_amt_4, pay_amt_5, pay_amt_6, default_payment_next_month`.
   
   - Pada kolom yang diambil diatas, terdapat beberapa kolom bertipe `STRING`. Pada saat pengambilan data dengan menggunakan perintah `SELECT`, lakukan konversi tipe data kolom-kolom bertipe `STRING` ke tipe numerik dengan panduan dibawah ini : 
     | Kolom | Tipe Data Awal | Tipe Data Akhir |
     | --- | --- | --- |
     | `sex` | STRING | INT |
     | `education_level` | STRING | INT |
     | `marital_status` | STRING | INT |
     | `pay_5` | STRING | FLOAT |
     | `pay_6` | STRING | FLOAT |
     | `default_payment_next_month` | STRING | INT |
   
   - Konversi tipe data harus dilakukan dalam sintaks yang sama saat melakukan query ke Google BigQuery.
   
   - Kolom diatas hanya digunakan sebagai dataset awal. Silakan lakukan Feature Selection di-notebook setelah dataset dibuat.
   
   - Limit jumlah data menjadi sebanyak `nomor batch dikali dengan tahun lahir kalian`. ex: Batch 10 dan lahir tahun 1995, 10 x 1995 = 19950.

4. Simpan dataset dalam bentuk csv, dengan nama `P1G5_Set_1_<nama-students>.csv`.

5. Salin query yang telah dibuat di Google Cloud Platform, tulislah pada bagian atas notebook !

6. Tampilkan `10 data pertama` dan `10 data terakhir` dari dataset pada notebook !

---

## Problems

Buatlah model Classification untuk memprediksi `default_payment_next_month` menggunakan dataset yang sudah kalian simpan.

---

## Conceptual Problems

_Jawab pertanyaan berikut:_

1. Apakah yang dimaksud dengan coeficient pada logistic regression?

2. Apakah fungsi parameter kernel pada SVM? Jelaskan salah satu kernel yang kalian pahami!

3. Bagaimana cara memilih `K` yang optimal pada KNN ?

4. Apa yang dimaksud dengan metrics-metrics berikut : `Accuracy`, `Precision`, `Recall`, `F1 Score`, dan kapan waktu yang tepat untuk menggunakannya ?

---

## Assignment Instructions

_Graded Challenge 5_ dikerjakan dalam format _notebook_ dengen beberapa **kriteria wajib** di bawah ini:

1. Machine learning framework yang digunakan adalah _Scikit-Learn_.

2. Ada penggunaan library visualisasi, seperti _matplotlib_, _seaborn_, atau yang lain.

3. Isi _notebook_ harus mengikuti _outline_ di bawah ini:
   1. Perkenalan
      > Bab pengenalan harus diisi dengan identitas, **query yang telah kalian buat pada Google Cloud Platform!**, dan _objective_ yang ingin dicapai.

   2. Query SQL
      > Tulis query yang telah dibuat untuk mengambil data dari Google Cloud Platform di bagian ini.

   3. Import Libraries
      > _Cell_ pertama pada _notebook_ **harus berisi dan hanya berisi** semua _library_ yang digunakan dalam _project_.

   4. Data Loading
      > Bagian ini berisi proses penyiapan data sebelum dilakukan eksplorasi data lebih lanjut. Proses Data Loading dapat berupa memberi nama baru untuk setiap kolom, mengecek ukuran dataset, dll.

   5. Exploratory Data Analysis (EDA)
      > Bagian ini berisi eksplorasi data pada dataset diatas dengan menggunakan query, grouping, visualisasi sederhana, dan lain sebagainya.

   6. Feature Engineering
      > Bagian ini berisi proses penyiapan data untuk proses pelatihan model, seperti pembagian data menjadi train-test, transformasi data (normalisasi, encoding, dll.), dan proses-proses lain yang dibutuhkan.

   7. Model Definition
      > Bagian ini berisi cell untuk mendefinisikan model. Jelaskan alasan menggunakan suatu algoritma/model, hyperparameter yang dipakai, jenis penggunaan metrics yang dipakai, dan hal lain yang terkait dengan model.

   8. Model Training
      > Cell pada bagian ini hanya berisi code untuk melatih model dan output yang dihasilkan. Lakukan beberapa kali proses training dengan hyperparameter yang berbeda untuk melihat hasil yang didapatkan. Analisis dan narasikan hasil ini pada bagian Model Evaluation.

   9. Model Evaluation
      > Pada bagian ini, dilakukan evaluasi model yang harus menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. Hal ini harus dibuktikan dengan visualisasi tren performa dan/atau tingkat kesalahan model. **Lakukan analisis terkait dengan hasil pada model dan tuliskan hasil analisisnya**.

   10. Model Saving
       > Pada bagian ini, dilakukan proses penyimpanan model dan file-file lain yang terkait dengan hasil proses pembuatan model. **Dengan melihat hasil Model Evaluation, pilihlah satu model terbaik untuk disimpan. Model terbaik ini akan digunakan kembali dalam melakukan Model Inference dan Model Deployment.**
   
   11. Model Inference
       > Model yang sudah dilatih akan dicoba pada data yang bukan termasuk ke dalam train-set ataupun test-set. Data ini harus dalam format yang asli, bukan data yang sudah di-scaled. Gunakan model terbaik berdasarkan hasil Model Evaluation.

   12. Pengambilan Kesimpulan
       > Pada bagian terakhir ini, **harus berisi** kesimpulan yang mencerminkan hasil yang didapat dengan _objective_ yang sudah ditulis di bagian pengenalan.

4. *Notebook* harus diupload dalam akun GitHub masing-masing student untuk selanjutnya dinilai.

---

## Assignment Submission

- Simpan assignment pada sesi ini dengan nama `P1G5_Set_1_<nama-student>.ipynb`, misal `P1G5_Set_1_raka_ardhi.ipynb`.

- Push Assigment yang telah Anda buat ke akun Github Classroom Anda masing-masing.

- Untuk Model Deployment :
  * Buat sebuah folder bernama `deployment` dan masukkan semua file yang berkaitan dengan deployment ke folder ini.
  * Buat sebuah file bernama `url.txt` yang berisi URL deployment.
  * Contoh bentuk isi repository dengan Model Deployment.
    ```
    ├── deployment/
    │   ├── app.py
    │   └── eda.py
    │   └── prediction.py
    │   └── model.pkl
    ├── P1G5_Set_1_raka_ardhi.ipynb
    ├── P1G5_Set_1_raka_ardhi.csv
    ├── url.txt
    └── README.md
    ```
---

## Assignment Rubrics

### Code Review

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| SQL | Mampu melakukan query data dengan kriteria yang telah diberikan | 15 pts |
| Feature Engineering | Mampu melakukan preprocessing dataset sebelum melakukan proses modeling (split data, normalisasi, encoding, dll) | 35 pts |
| Logistic Regression | Mengimplementasikan Logistic Regression dan menentukan hyperparameter yang tepat dengan Scikit-Learn | 5 pts |
| SVM | Mengimplementasikan SVM dan menentukan hyperparameter yang tepat dengan Scikit-Learn | 5 pts |
| KNN | Mengimplementasikan KNN dan menentukan hyperparameter yang tepat dengan Scikit-Learn | 5 pts |
| Hyperparameter Tuning | Mengimplementasikan Hyperparameter Tuning dengan Scikit-Learn | 20 pts |
| Model Inference | Mencoba model yang telah dibuat dengan data baru | 10 pts |
| Runs Perfectly | Kode berjalan tanpa ada error. Seluruh kode berfungsi dan dibuat dengan benar | 10 pts |

### Concepts

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Classifications | Mampu menjawab pertanyaan dengan singkat, jelas, dan padat serta sesuai dengan konsep dan logika yang ada mengenai Conceptual Problems (10 each number) | 40 pts |

### Readability

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Tertata Dengan Baik | Semua baris kode terdokumentasi dengan baik dengan Markdown untuk penjelasan kode | 15 pts |

```
Kriteria tertata dengan baik diantaranya adalah: 

1. Terdapat section Perkenalan yang jelas dan lengkap terkait masalah dan latar belakang masalah yang akan diselesaikan.
2. Tidak menyalin markdown dari tugas lain.
3. Import library rapih (terdapat dalam 1 cell dan tidak ada unused libs).
4. Pemakaian fungsi markdown yang optimal (Heading, text formating, dll).
5. Terdapat komentar pada setiap baris kode.
6. Adanya pemisah yang jelas antar section, dll.
7. Tidak adanya typo.
```

### Analysis

| Criteria | Meet Expectations | Points|
| --- | --- | --- |
| Model Analysis | Menganalisa informasi dari model yang telah dibuat | 35 pts |
| Overall Analysis | Menarik informasi/kesimpulan dari keseluruhan kegiatan yang dilakukan | 20 pts |

```
Contoh kriteria analisa yang baik diantaranya adalah: 

1. Terdapat penjelasan macam-macam hasil metric evaluasi dan interpretasinya terhadap kasus yang diselesaikan.
2. Dapat menjelaskan KELEBIHAN dan KELEMAHAN dari model yang dibuat DENGAN KAITANNYA DENGAN DOMAIN BUSINESS YANG DIHADAPI yang dibuktikan dengan eksplorasi sederhana (grafik, plot, teori, dll).
3. Dapat memberikan statement untuk improvement selanjutnya dari model yang dibuat. 
4. Dapat menyebutkan insight yang dapat diambil setelah proses EDA, dll.
```

### Model Deployment

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Model Deployment | Membuat webapps terhadap project yang telah dibuat | 15 pts |

```
Catatan mengenai Model Deployment : 

1. Ketiadaan URL deployment ataupun source code deployment di repository, akan tetap diperhitungkan untuk menilai bagian Model Deployment. 
2. Tidak diperkenankan adanya informasi tambahan/informasi susulan seperti lupa memberikan URL deployment atau lupa mengupload source code via apapun (DM buddy, email, atau yang lain).
3. Student akan dianggap tidak melakukan Model Deployment jika tidak ada URL deployment dan source code deployment di repository.
```

---

```
Total Points : 230
```

---

## Notes

- **Deadline : P1W3D1 pukul 23:59 WIB.**

- **Keterlambatan pengumpulan tugas mengakibatkan skor Graded Challenge 5 menjadi 0.**
