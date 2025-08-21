from datetime import datetime
import os

# Class Buku
class Buku:
    def __init__(self, isbn, judul, pengarang, jumlah, terpinjam):
        self.isbn = isbn
        self.judul = judul
        self.pengarang = pengarang
        self.jumlah = jumlah
        self.terpinjam = terpinjam

    def tampil(self):
        print(f"{self.isbn}\t{self.judul}\t{self.pengarang}\t{self.jumlah}\t{self.terpinjam}")

# Class Peminjaman
class Peminjaman:
    def __init__(self, isbn, status, tanggal_pinjam, tanggal_kembali=""):
        self.isbn = isbn
        self.status = status
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali

    def tampil(self):
        print(f"{self.isbn}\t{self.status}\t{self.tanggal_pinjam}\t{self.tanggal_kembali}")

# Data Awal
books = [
    Buku("9786237121144", "Kumpulan Solusi Pemrograman Python", "Budi Raharjo", 6, 0),
    Buku("9786231800718", "Dasar-Dasar Pengembangan Perangkat Lunak dan Gim Vol. 2", "Okta Purnawirawan", 15, 0),
    Buku("9786026163905", "Analisis dan Perancangan Sistem Informasi", "Adi Sulistyo Nugroho", 2, 1),
    Buku("9786022912828", "Animal Farm", "George Orwell", 4, 0)
]

records = [
    Peminjaman("9786022912828", "Selesai", "2025-03-21", "2025-03-28"),
    Peminjaman("9786026163905", "Belum", "2025-07-22")
]

# Fungsi Utility
def bersih():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menu dan Fungsi Operasi
def tampilkan_data():
    print("\nDAFTAR BUKU:")
    for i, buku in enumerate(books, 1):
        print(i, end="\t")
        buku.tampil()
    print("====================================================================\n")

def tambah_data():
    print("\nTAMBAH DATA BUKU")
    isbn = input("Masukkan ISBN: ")
    judul = input("Masukkan Judul: ")
    pengarang = input("Masukkan Pengarang: ")
    jumlah = int(input("Masukkan Jumlah: "))
    terpinjam = int(input("Masukkan Terpinjam: "))
    buku_baru = Buku(isbn, judul, pengarang, jumlah, terpinjam)
    books.append(buku_baru)
    print("Data berhasil ditambahkan.\n")

def edit_data():
    tampilkan_data()
    index = int(input("Pilih nomor buku yang ingin diubah: ")) - 1
    if 0 <= index < len(books):
        buku = books[index]
        buku.isbn = input("Masukkan ISBN baru: ")
        buku.judul = input("Masukkan Judul baru: ")
        buku.pengarang = input("Masukkan Pengarang baru: ")
        buku.jumlah = int(input("Masukkan Jumlah baru: "))
        buku.terpinjam = int(input("Masukkan jumlah Terpinjam baru: "))
        print("Data berhasil diubah.\n")
    else:
        print("Indeks tidak valid.\n")

def hapus_data():
    tampilkan_data()
    index = int(input("Pilih nomor buku yang ingin dihapus: ")) - 1
    if 0 <= index < len(books):
        del books[index]
        print("Data berhasil dihapus.\n")
    else:
        print("Indeks tidak valid.\n")

def tampilkan_peminjaman():
    print("\nDAFTAR PEMINJAMAN:")
    for i, r in enumerate(records, 1):
        print(i, end="\t")
        r.tampil()
    print("====================================================================\n")

def tampilkan_belum():
    print("\nDAFTAR BELUM DIKEMBALIKAN:")
    ditemukan = False
    for i, r in enumerate(records, 1):
        if r.status.lower() == "belum":
            print(i, end="\t")
            r.tampil()
            ditemukan = True
    if not ditemukan:
        print("Semua buku sudah dikembalikan.")
    print("====================================================================\n")

def peminjaman():
    print("\nPEMINJAMAN BUKU")
    isbn = input("Masukkan ISBN buku yang dipinjam: ")
    tanggal_pinjam = input("Masukkan tanggal pinjam (YYYY-MM-DD): ")
    tanggal_kembali = input("Masukkan tanggal kembali (YYYY-MM-DD): ")
    records.append(Peminjaman(isbn, "Belum", tanggal_pinjam, tanggal_kembali))
    # Update buku terpinjam
    for buku in books:
        if buku.isbn == isbn:
            buku.terpinjam += 1
    print("Peminjaman berhasil ditambahkan.\n")

def pengembalian():
    tampilkan_peminjaman()
    index = int(input("Pilih nomor peminjaman yang ingin dikembalikan: ")) - 1
    if 0 <= index < len(records):
        records[index].status = "Selesai"
        records[index].tanggal_kembali = input("Masukkan tanggal kembali (YYYY-MM-DD): ")
        # Update buku terpinjam
        for buku in books:
            if buku.isbn == records[index].isbn:
                buku.terpinjam -= 1
        print("Pengembalian berhasil.\n")
    else:
        print("Indeks tidak valid.\n")

def menu():
    while True:
        print("---=== MENU ===---")
        print("[1] Tampilkan Data")
        print("[2] Tambah Data")
        print("[3] Edit Data")
        print("[4] Hapus Data")
        print("[5] Tampilkan Semua Peminjaman")
        print("[6] Tampilkan Peminjaman Belum Kembali")
        print("[7] Peminjaman")
        print("[8] Pengembalian")
        print("[X] Keluar")

        pilih = input("Masukkan pilihan menu (1-8 atau X): ").lower()

        bersih()
        if pilih == "1":
            tampilkan_data()
        elif pilih == "2":
            tambah_data()
        elif pilih == "3":
            edit_data()
        elif pilih == "4":
            hapus_data()
        elif pilih == "5":
            tampilkan_peminjaman()
        elif pilih == "6":
            tampilkan_belum()
        elif pilih == "7":
            peminjaman()
        elif pilih == "8":
            pengembalian()
        elif pilih == "x":
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid.\n")

# Jalankan Program
menu()
