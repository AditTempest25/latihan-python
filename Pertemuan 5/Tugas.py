# Ketua Kelompok : Aditya Putra Aji Nur Alamsyah
# Anggota Kelompok :
#     - Yufry
#     - Ayu Raditha Putri Budiman

# ============================================================
# MENU disimpan sebagai dictionary
# Format: "kode": ("nama potongan", harga_satuan)
# ============================================================
MENU = {
    "D": ("Dada",  2500),
    "P": ("Paha",  2000),
    "S": ("Sayap", 1500),
}
# ============================================================
# FUNGSI format_rupiah(angka)
# Mengubah angka biasa menjadi format mata uang rupiah
# Contoh: 2500 → "Rp 2.500"
# 
# Cara kerjanya:
#   f"Rp {angka:,.0f}" → menghasilkan "Rp 2,500" (koma sebagai pemisah ribuan)
#   .replace(",", ".") → mengganti koma jadi titik → "Rp 2.500" (format Indonesia)
# ============================================================
def format_rupiah(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")
# ============================================================
# FUNGSI get_int(prompt, min_val)
# Fungsi untuk meminta input angka bulat dari user dengan validasi
#
# Parameter:
#   prompt   -> teks yang ditampilkan ke user saat meminta input
#   min_val  -> nilai minimum yang diperbolehkan (default = 1)
#
# Cara kerjanya:
#   - Pakai loop "while True" supaya terus minta input sampai valid
#   - try/except untuk menangkap error kalau user input bukan angka
#   - Kalau angka < min_val, minta input ulang
# ============================================================
def get_int(prompt, min_val=1):
    while True:
        try:
            nilai = int(input(prompt))        
            if nilai >= min_val:
                return nilai                  
            print(f"Input harus minimal {min_val}, coba lagi!")
        except ValueError:
            print("Input harus berupa bilangan bulat")
# ============================================================
# FUNGSI tampilkan_menu()
# Mencetak daftar menu ke layar dalam bentuk tabel
#
# Cara kerjanya:
#   - Loop ke setiap item di MENU menggunakan .items()
#   - .items() menghasilkan pasangan key & value -> (kode, (nama, harga))
# ============================================================
def tampilkan_menu():
    print("\nGEOBAK FRIED CHICKEN")
    print("-" * 52)
    print(f"{'Kode':<6}{'Jenis Potongan':<18}{'Harga'}")
    print("-" * 52)
    for kode, (nama, harga) in MENU.items():
        print(f"{kode:<6}{nama:<18}{format_rupiah(harga)}")
    print("-" * 52)
# ============================================================

# ============================================================

# Tampilkan menu dulu sebelum input
tampilkan_menu()

# Minta input jumlah jenis potongan (minimal 1)
jumlah_potongan = get_int("Masukkan Banyak Jenis Potongan Yang Ingin Dibeli : ")

# Siapkan list kosong untuk menyimpan semua item yang dibeli
# dan variabel totalbayar untuk akumulasi harga
data       = []
totalbayar = 0

# ============================================================
# LOOP INPUT ITEM
# Perulangan sebanyak jumlah_potongan yang diinput user
# ============================================================
for i in range(jumlah_potongan):
    print(f"\n-- Item ke-{i + 1} --")

    # --- Validasi jenis potongan ---
    # Loop terus sampai user input kode yang ada di MENU (D, P, atau S)
    while True:
        jenis = input("Masukkan Jenis Potongan (D/P/S)       : ").upper().strip()
        # .upper()  -> ubah ke huruf besar supaya "d" sama dengan "D"
        # .strip()  -> hapus spasi di awal/akhir input
        if jenis in MENU:
            break                             
        print(f"Jenis '{jenis}' tidak tersedia. Pilih D, P, atau S.")

    # Minta jumlah beli (minimal 1)
    banyak = get_int("Masukkan Jumlah Potongan               : ")

    # Ambil nama dan harga dari MENU sesuai kode yang diinput
    # Contoh: jenis = "D" maka nama_potongan = "Dada", harga = 2500
    nama_potongan, harga = MENU[jenis]

    # Hitung subtotal item ini
    jumlahbayar  = harga * banyak

    # Tambahkan subtotal ke total keseluruhan
    # += adalah singkatan dari totalbayar = totalbayar + jumlahbayar
    totalbayar += jumlahbayar

    # Simpan data item ke dalam list sebagai tuple (Ini ada di pertemuan 6)
    # Tuple dipilih karena data item tidak akan diubah lagi setelah disimpan
    data.append((i + 1, nama_potongan, harga, banyak, jumlahbayar))


# ============================================================
# CETAK STRUK
# ============================================================
print("\nGEROBAK FRIED CHICKEN")
print("-" * 62)
# Header tabel — angka :<N menentukan lebar tiap kolom
print(f"{'No':<5}{'Jenis':<14}{'Harga Satuan':<16}{'Banyak':<10}{'Subtotal'}")
print("-" * 62)

# Loop ke setiap item yang sudah disimpan di list data
# Unpack tuple langsung di for supaya kodenya lebih bersih
for no, nama, harga, banyak, subtotal in data:
    print(f"{no:<5}{nama:<14}{format_rupiah(harga):<16}{banyak:<10}{format_rupiah(subtotal)}")

print("-" * 62)

# ============================================================
# PERHITUNGAN PAJAK & TOTAL AKHIR
# pajak    = 10% dari totalbayar
# totalakhir = totalbayar + pajak
# ============================================================
pajak      = totalbayar * 0.1
totalakhir = totalbayar + pajak

# Cetak ringkasan biaya
# :<30 -> rata kiri dengan lebar 30 karakter supaya titik dua sejajar
print(f"{'Subtotal':<30}: {format_rupiah(totalbayar)}")
print(f"{'Pajak (10%)':<30}: {format_rupiah(pajak)}")
print(f"{'Total Akhir':<30}: {format_rupiah(totalakhir)}")
print("-" * 62)

# ============================================================
# INPUT PEMBAYARAN
# min_val diisi totalakhir supaya uang yang diinput pasti cukup
# int() dipakai karena get_int() butuh integer, bukan float
# ============================================================
bayar     = get_int("Uang Bayar                             : Rp ", min_val=int(totalakhir))
kembalian = bayar - totalakhir 

# Cetak hasil pembayaran
print(f"{'Uang Bayar':<30}: {format_rupiah(bayar)}")
print(f"{'Kembalian':<30}: {format_rupiah(kembalian)}")
print("-" * 62)
print("Terima kasih telah berbelanja!")

