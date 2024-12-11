# Kalkulator Python

## Deskripsi
Proyek ini adalah sebuah aplikasi kalkulator sederhana berbasis **CLI (Command Line Interface)** yang dibuat menggunakan Python. Kalkulator ini mendukung operasi matematika dasar seperti penjumlahan, pengurangan, perkalian, dan pembagian. Selain itu, program ini dilengkapi dengan fitur riwayat perhitungan, tutorial, serta informasi kontak developer.

Proyek ini merupakan **Project Akhir 2024** dari **11 TKJ 1 SMEKSA**.

---

## Fitur
- **Perhitungan Dasar**: Penjumlahan (+), Pengurangan (-), Perkalian (*), dan Pembagian (/).
- **Riwayat Perhitungan**:
  - Menampilkan riwayat perhitungan.
  - Mengedit atau menghapus riwayat perhitungan.
- **Interaktif**:
  - Menu Tutorial.
  - Menu Kontak Developer.
- **Efek Visual**:
  - Warna-warna menarik di terminal menggunakan modul `colorama` dan `pystyle`.

---

## Tampilan Program
### Tampilan Awal
Tambahkan gambar tampilan awal program Anda di bawah ini:  
![Tampilan Awal](path/to/image1.jpg)

### Riwayat Perhitungan
Tambahkan gambar contoh tampilan riwayat perhitungan di bawah ini:  
![Riwayat Perhitungan](path/to/image2.jpg)

---

## Cara Menggunakan
1. **Jalankan Program**:
   - Pastikan Python terinstal di komputer Anda.
   - Jalankan program dengan mengetik:
     ```bash
     python kalkulator.py
     ```

2. **Navigasi Menu**:
   - Ketik bilangan atau ekspresi matematika langsung (contoh: `48+22-80/2*6`) untuk melakukan perhitungan.
   - Gunakan menu interaktif:
     - `1`: Melihat tutorial penggunaan.
     - `2`: Melihat, mengedit, atau menghapus riwayat perhitungan.
     - `3`: Melihat informasi kontak author.
     - `4`: Keluar dari program.

3. **Fitur Riwayat**:
   - Pilih menu `2` untuk melihat riwayat perhitungan.
   - Anda dapat:
     - Mengedit riwayat dengan memilih `edit` dan memasukkan perhitungan baru.
     - Menghapus riwayat dengan memilih `hapus`.
     - Keluar dari menu riwayat dengan memilih `tidak`.

---

## Dependencies
Program ini menggunakan beberapa modul Python. Pastikan semua modul berikut sudah terinstal:
- **os**: Modul bawaan untuk operasi sistem.
- **sys**: Modul bawaan untuk mengakses fungsi interpreter Python.
- **time**: Modul bawaan untuk kontrol waktu.
- **pystyle**: Untuk memberikan warna dan efek gaya pada terminal.
- **colorama**: Untuk menambahkan warna pada output terminal.

### Instalasi Dependencies
Gunakan perintah berikut untuk menginstal dependencies:
```bash
pip install pystyle colorama
