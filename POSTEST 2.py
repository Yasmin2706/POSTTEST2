# Agar tampilan lebih rapi dan bersih
import os
os.system ('cls')

# Import prettytable
from prettytable import PrettyTable 

# Menyambut dengan hangat
print("==============SELAMAT DATANG DI TOKO EMPAT LIMA TEKSTIL==============")
print("==================Toko Kain Bahan Tekstil Lengkap====================")

# Jenis kain yang tersedia di toko
kain = [
    ["katun", "Rp8000 ", "1 meter", "20"],
    ["rayon", "Rp10000", "1.5 meter", "15"],
    ["wol", "Rp12000", "0.5 meter", "14"],
    ["sutra","Rp14000", "0.5 meter", "15"],
    ["linen","Rp14000", "2 meter", "15"],
    ["denim","Rp16000", "1.5 meter", "10"]
]

# Password dan username untuk login sebagai admin atau pembeli
user_login = {
    "mimintekstil" : "admintekstilkece",
    "buyertekstil" : "pembelikece"
}

# ===============================ADMIN======================================
# Admin dapat menampilkan, menambah, mengubah, dan menghapus produk

# Jika admin ingin menampilkan tabel maka memakai function berikut
def tampilkan_kain():
    table_kain = PrettyTable()
    table_kain.field_names = ["Jenis kain", "Harga", "Panjang Kain Minimal", "Jumlah Tersedia"]
    for item in kain:
        table_kain.add_row(item)
    print(table_kain)

# Jika admin ingin menambahkan produk ke tabel maka memakai function berikut
def menambah() :
    nama_kain = input("Masukkan nama jenis kain: ")
    harga = input("Masukkan harga jenis kain: ")
    panjang_kain_minimal = input("Masukkan panjang kain minimal: ")
    jumlah_yang_tersedia = input("Jumlah jenis kain yang tersedia: ")
    tambahan = [nama_kain, harga, panjang_kain_minimal, jumlah_yang_tersedia]
    kain.append(tambahan)
    tampilkan_kain()

# Jika admin ingin mengubah produk di tabel maka memakai function berikut
def mengubah() :
    produk = str(input("Masukkan nama jenis kain yang ingin diubah: "))
    for i in range(len(kain)):
        if kain[i][0] == produk:
            nama_kain = input("Masukkan nama jenis kain baru: ")
            harga = input("Masukkan harga jenis kain baru: ")
            panjang_kain_minimal = input("Masukkan panjang kain minimal: ")
            jumlah_yang_tersedia = input("Masukkan stok: ")
            kain[i][0] = nama_kain
            kain[i][1] = harga
            kain[i][2] = panjang_kain_minimal
            kain[i][3] = jumlah_yang_tersedia
            print(f"Data berhasil diubah dari {produk} menjadi kain yang diinginkan")
            tampilkan_kain()
            break
    else:
        print(f"{produk} produk kain tidak dapat ditemukan")

# Jika admin ingin menghapus produk di tabel maka memakai function berikut
def menghapus() :
    produk = str(input("Masukkan nama jenis kain yang ingin dihapus: "))
    salah = False

    for i in range(len(kain)):
        if kain[i][0] == produk:
            del kain[i]
            salah = True
            break

    if salah:
        print(f"{produk} telah dihapus.")
        tampilkan_kain()
    else:
        print(f"{produk} tidak ditemukan.")

# Tampilan jika login sebagai admin

def admintekstil() :
        while True:
            print("=====================================================================")
            print("|                              Menu admin                           |")
            print("=====================================================================")
            print("Hai Admin! Semangat kerjanya dan ucapkan Bismillah untuk memulai hari")
            print("Di sini mimin tekstil mau ngapain?")
            print("1. Tampilkan produk kain")
            print("2. Tambah produk kain")
            print("3. Update produk kain")
            print("4. Hapus produk kain")
            print("5. Keluar")
            pilihan = input("Masukkan pilihan (1/2/3/4/5) : ")

            if pilihan == "1":
                tampilkan_kain()
            elif pilihan == "2":
                tampilkan_kain()
                menambah()
            elif pilihan == "3":
                tampilkan_kain()
                mengubah()
            elif pilihan == "4":
                tampilkan_kain()
                menghapus()
            elif pilihan == "5":
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")

# ===============================PEMBELI======================================
# Tampilan jika login sebagai pembeli

def pembelitekstil():
    print("=====================================================================")
    print("|                         TOKO EMPAT LIMA TEKSTIL                   |")
    print("|                     Toko Kain Bahan Tekstil Lengkap               |")
    print("|                     SELAMAT BERBELANJA DI TOKO KAMI               |")
    print("=====================================================================")
    print()
    tampilkan_kain()
    while True:
        produk = str(input("Pilih nama jenis kain yang ingin dibeli: "))
        for i in range(len(kain)):
            if kain[i][0] == produk:
                nama_produk = kain[i][0]
                harga_produk = kain[i][1]
                print(f"Anda membeli {nama_produk} seharga {harga_produk}.")
        while True:
            pilihan = input("Apakah ada kain yang ingin Anda beli lagi? (y/t): ").lower()
            if pilihan == "t":
                print("Terima kasih telah berbelanja di '45 Tekstil'")
                return
            elif pilihan == "y":
                break
            else:
                print("Pilihan tidak tersedia")

# Function untuk login
def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in user_login and user_login[username] == password:
        if username == "mimintekstil":
            print("Selamat datang, Admin Tercinta! Semangat kerjanya!")
            admintekstil()
        else:
            print("Selamat datang, Pembeli Terhormat! Semoga puas dengan layanan kami!")
            pembelitekstil()
    else:
        print("Login tidak berhasil. Mohon dicoba kembali.")

# Function untuk memilih peran
while True:
    print("=====================================================================")
    print("Halo!")
    print("Mohon pilih peran Anda:")
    print("1. Login sebagai admin")
    print("2. Login sebagai pembeli")
    print("3. Keluar")
    peran = int(input("Pilih peran pada menu login (1/2/3): "))
    
    if peran == 1:
        login()
    elif peran == 2:
        login()
    elif peran == 3:
        print("Terima kasih! Sampai jumpa lagi! :D ")
        break
    else:
        print("Pilihan peran tidak valid. Mohon dicoba kembali.")