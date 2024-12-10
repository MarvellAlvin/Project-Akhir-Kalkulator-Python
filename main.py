#since 2024
#11 TKJ 1 SMEKSA

# Untuk Mengimport Modul
import os #vModul os untuk mengimport path pada suatu file atau script
import sys # Modul sys untuk menyediakan akses ke variabel dan fungsi yang terkait dengan interpreter pada Python
import time # Modul time untuk menyediakan fungsi yang mengontrol waktu.
from pystyle import Colorate, Colors
from colorama import Fore,Back,init,Style # Modul Colorama untuk menambahkan warna pada Python.

def autoketik(s): # Fungsi pada string (s) sebagai input dan secara bertahap mencetak karakter-karakter dalam string tersebut ke terminal dengan penundaan waktu tertentu. Ini menciptakan efek "auto-typing".
    for c in s + "\n": # Fungsi ini mengiterasi setiap karakter dalam string s ditambah dengan karakter newline (\n) untuk pindah ke baris baru.
        sys.stdout.write(c) # Setiap karakter ditulis ke output standar.
        sys.stdout.flush() # Memastikan tampilan segera.
        time.sleep(0.005) # Fungsi ini digunakan untuk menunda eksekusi selama 0.008 detik. Menciptakan efek "ketikan" yang lambat dan terlihat nyata.

# Warna
B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW

# Warna kode ANSI escape sequence
hijau="\033[1;92m "
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="\033[1;91m"
biru="\033[1;96m"

#Teks Pada Awal Kode Saat Di Run
os.system("clear") # Untuk Menghapus Semua Elemen Dari Suatu Set, Sehingga Menghasilkan Set Yang Kosong
autoketik(f"{W}[{R}•{W}] {kuning}Loading...") # Fungsi yang telah didefinisikan sebelumnya untuk menampilkan teks secara bertahap, memberikan efek "mengetik".
#time.sleep(1) # Fungsi ini membuat program berhenti selama 1 detik sebelum menampilkan pesan berikutnya, memberikan efek jeda.
#autoketik(f"{W}[{R}•{W}] {G}Jangan Lupa Follow {biru}marpell.xyz") # f-string yang digunakan untuk membuat format teks dengan warna yang berbeda. variabel W, R, G, biru, dll, berisi kode warna untuk terminal.
#url_instagram = "https://www.instagram.com/marpell.xyz" # Variabel yang menyimpan URL Instagram.
#os.system(f"xdg-open {url_instagram}") # Fungsi ini digunakan untuk menjalankan perintah sistem dan perintah untuk membuka URL menggunakan aplikasi default. xdg-open adalah perintah umum di sistem operasi berbasis Unix.
#time.sleep(1)
#autoketik(f"{W}[{R}•{W}] {kuning}Terimakasih {ungu}>_<{G}")
time.sleep(1)
os.system("clear") # Fungsi yang dasarnya mengirim oerintah clear untuk membersihkan layar, menghapus semua teks, dan memindahkan kursor ke sudut kiri atas.


history = {}  # Menggunakan kamus untuk menyimpan riwayat dengan nomor urut
print(Colorate.Horizontal(Colors.cyan_to_green,"""

██╗  ██╗ █████╗ ██╗     ██╗  ██╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
██║ ██╔╝██╔══██╗██║     ██║ ██╔╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
█████╔╝ ███████║██║     █████╔╝ ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
██╔═██╗ ██╔══██║██║     ██╔═██╗ ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
██║  ██╗██║  ██║███████╗██║  ██╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                   
        ╔═════════════════════════════════════════════════╗
        ║                                                 ║
        ║  - 1 |  Tutorial                                ║ 
        ║  - 2 |  History                                 ║
        ║  - 3 |  Kontak                                  ║
        ║  - 4 |  Keluar                                  ║
        ║                                                 ║
        ║  - Kalkulator Python v.1                        ║
        ║  - Project Akhir 2024                           ║
        ║                                                 ║  
        ╚═════════════════════════════════════════════════╝

"""))
print(Colorate.Horizontal(Colors.cyan_to_green,"\n[+] Pilih menu atau masukan bilangan yang ingin dikalkulasikan"))          
while True:
    user_input = input(Colorate.Horizontal(Colors.cyan_to_green,"\nroot@home:~$ "))
    
    if user_input.lower() == '2':
        if history:
            for index, item in history.items():
                print(f"{index}. {item}")
            edit_or_delete = input("Ingin edit atau hapus riwayat?\n(edit,hapus,tidak)\nroot@history:~$ ")
            if edit_or_delete.lower() == 'edit':
                index_to_edit = int(input("Masukkan nomor riwayat yang ingin diedit: "))
                new_expression = input("Masukkan perhitungan baru: ")
                try:
                    new_result = eval(new_expression)
                    history[index_to_edit] = f"{new_expression} = {new_result}"
                    print(f"{ungu}Riwayat berhasil diedit.")
                except Exception as e:
                    print(f"{R}Terjadi kesalahan:", e)
            elif edit_or_delete.lower() == 'hapus':
                index_to_delete = int(input("Masukkan nomor riwayat yang ingin dihapus: "))
                del history[index_to_delete]
                print(f"{ungu}Riwayat berhasil dihapus.")
        else:
            autoketik(Fore.RED + 'Tidak ada riwayat perhitungan.')
            autoketik(Fore.YELLOW + "Silahkan melakukan perhitungan terlebih dahulu")
            print(f"{W}Contoh: 48+22-80/2*6")
            
    elif user_input.lower() == '1':
        os.system("clear")
        print(f"{G}╔═══{W}[ {ungu}Tutorial {W}]\n{G}║ {R}• {Y}Input bilangan yang ingin di kalkulasikan\n{G}║ {R}• {Y}Contoh: 4+4\n{G}║ {R}• {Y}Anda juga bisa melakukan perhitungan secara gabungan\n{G}║ {R}• {Y}Contoh: 4+4-3 atau 4+4-3*5/2\n{G}╚══> \n{G}╔═══{W}[ {ungu}Riwayat {W}]\n{G}║ {R}• {Y}Sebelum cek riwayat, silahkan melakukan perhitungan terlebih dahulu.\n{G}║ {R}• {Y}Jika sudah mempunyai riwayat perhitungan silahkan ingin di edit atau tidak.\n{G}║ {R}• {Y}Jika ada yang ingin di edit silahkan input nomor riwayat yang tertera.\n{G}║ {R}• {Y}Input (edit) untuk mengedit riwayat perhitungan yang sebelumnya anda buat\n{G}║ {R}• {Y}Contoh: awal perhitungan 4+4 diubah menjadi 4*4\n{G}║ {R}• {Y}Input (hapus) untuk menghapus riwayat.\n{G}║ {R}• {Y}Input (tidak) untuk keluar dari menu riwayat.\n{G}╚══>\n{G}╔═══{W}[ {ungu}Informasi {W}]\n{G}║ {R}• {Y}(+) untuk menjumlahkan.\n{G}║ {R}• {Y}(-) untuk pengurangan.\n{G}║ {R}• {Y}(*) untuk perkalian.\n{G}║ {R}• {Y}(/) untuk pembagian.\n{G}║ {R}• {Y}Input 2 untuk riwayat perhitungan.\n{G}║ {R}• {Y}Input 3 untuk informasi kontak author.\n{G}║ {R}• {Y}Input 4 untuk keluar dari program kalkulator.\n{G}║ {R}• {Y}Atau langsung masukan perhitungan.\n{G}╚══> ")
       
    elif user_input.lower() == '3':
        os.system("clear")
        print(Colorate.Horizontal(Colors.cyan_to_green,"""

        ███╗   ███╗ █████╗ ██████╗ ██████╗ ███████╗██╗     
        ████╗ ████║██╔══██╗██╔══██╗██╔══██╗██╔════╝██║     
        ██╔████╔██║███████║██████╔╝██████╔╝█████╗  ██║     
        ██║╚██╔╝██║██╔══██║██╔══██╗██╔═══╝ ██╔══╝  ██║     
        ██║ ╚═╝ ██║██║  ██║██║  ██║██║     ███████╗███████╗
        ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚══════╝
                                                   
     
            ╔════════════════════════╗
            ║      [admin123]        ║          https://github.com/MarvellAlvin
            ║      marvellawm        ║          https://www.instagram.com/marpell_xyz
            ╚════════════════════════╝            
                     
"""))
    
    elif user_input.lower() == '4':
        print(Colorate.Horizontal(Colors.cyan_to_green,"root@marpel:~$ Terima kasih telah menggunakan kalkulator!"))
        break  # Keluar dari loop
            
    else: # Blok ini dijalankan jika input pengguna tidak cocok dengan kondisi sebelumnya
        try:
            # Mengevaluasi ekspresi matematika yang dimasukkan pengguna
            result = eval(user_input) # Menghitung hasil ekspresi yang diberikan oleh pengguna
            # Menyimpan ekspresi dan hasilnya ke dalam riwayat perhitungan
            history[len(history) + 1] = f"{user_input} = {result}" # Key adalah nomor urut, value adalah ekspresi dan hasilnya
            print("Hasilnya adalah:", result) # Menampilkan hasil perhitungan ke pengguna
        except Exception as e: # Menangkap kesalahan jika `eval` gagal dijalankan
            print("Terjadi kesalahan:", e) # Menampilkan pesan kesalahan dan jenis kesalahan
