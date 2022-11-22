## Algeo-Tubes02
## TUGAS BESAR 2 IF2123 ALJABAR LINIER DAN GEOMETRI : Face Recognition dengan Eigenface
### SEMESTER 1 TAHUN 2022/2023
<br>

### Kelompok 45
 Disusun Oleh : 
 - 13521112 Rayhan Hanif Maulana Pradana
 - 13521159 Sulthan Dzaky Alfaro
 - 13521168 Satria Octavianus Nababan
<br>
<br>


### Table of Contents
  1. [Prasyarat](#prasyarat)
  2. [Cara Clone Program](#cara-clone-program)
  3. [Cara Menjalankan Program](#cara-menjalankan-program)
  4. [Menu](#menu)
  5. [Contoh Penggunaan](#contoh-penggunaan)

<br>

### Prasyarat
Telah mengunduh python versi 3.4 ke atas. Jika belum, silahkan unduh pada tautan berikut

<a href="https://www.python.org/downloads/" target="_blank"></a>

Unduh package OpenCV, tkinter, dan numpy dengan menjalankan perintah berikut

```sh
pip install opencv-python

pip install tk

pip install numpy

pip install pillow
```

<br>

<br>

### Cara Clone Program
Clone dilakukan agar program/aplikasi dapat dijalankan pada mesin Anda.
Jalankan perintah berikut pada terminal

```sh
git clone https://github.com/rayhanp1402/Algeo02-21112.git
```
<br>

<br>

### Cara Menjalankan Program
Pindah ke directory tempat Anda clone program pada terminal, contoh :

```sh
cd /mnt/c
```

Jika sudah berada pada directory yang dimaksud, jalankan perintah-perintah berikut

```sh
cd Algeo02-21112/src

python GUI.py
```

<br>

<br>

### Menu
Tampilan menu program
<br>

![Menu](https://cdn.discordapp.com/attachments/865154167169351730/1044550752875593738/face_recognition_menu.jpg)

<br>

<br>

### Contoh Penggunaan
Klik select pada "Input training image"

<br>

![Input1](https://cdn.discordapp.com/attachments/865154167169351730/1044551291168379021/face_recognition_dataset.jpg)

<br>

Pilih folder dataset (telah diekstraksi dengan nilai 256 x 256 pixel) yang ingin digunakan untuk training

<br>

![Dataset](https://cdn.discordapp.com/attachments/865154167169351730/1044552046386356244/face_recognition_datasetfolder.jpg)

<br>

Tunggu beberapa detik. Jika terlihat tulisan "mantap" sebagai berikut

<br>

![Mantap](https://cdn.discordapp.com/attachments/865154167169351730/1044551650913832991/face_recognition_mantap.jpg)

<br>

Proses training sudah selesai. Kemudian, klik select pada "Input test image"

<br>

![Input2](https://cdn.discordapp.com/attachments/865154167169351730/1044551759131050064/face_recognition_test.jpg)

<br>

Pilih foto yang ingin dikenali

<br>

![Foto](https://cdn.discordapp.com/attachments/865154167169351730/1044552160043601950/face_recognition_testimage.jpg)

<br>

Hasil

<br>

![Hasil](https://cdn.discordapp.com/attachments/865154167169351730/1044551883274059816/face_recognition_hasil.jpg)