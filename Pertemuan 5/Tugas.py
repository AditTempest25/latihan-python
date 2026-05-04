# Ketua Kelompok : Aditya Putra Aji Nur Alamsyah
# Anggota Kelompok : 
#     - Yufry
#     - Ayu Raditha Putri Budiman
def format_rupiah(angka):
    return f"Rp {angka:,.0f}".replace(",", ".") # Fungsi untuk mengubah angka menjadi rupiah agar lebih rapih

print("GEROBAK FRIED CHICKEN")
print("-" * 50)
print("Kode JenisPotongan Harga")
print("-" * 50)
print(f"{'D':<5}{'Dada':<15}{'Rp. 2500'}") # Fungsi Dari <5 atau <15 berfungsi untuk memberikan space atau ruang pada tiap kolom
print(f"{'P':<5}{'Paha':<15}{'Rp. 2000'}") # Fungsi Dari <5 atau <15 berfungsi untuk memberikan space atau ruang pada tiap kolom
print(f"{'S':<5}{'Sayap':<15}{'Rp. 1500'}") # Fungsi Dari <5 atau <15 berfungsi untuk memberikan space atau ruang pada tiap kolom
print("-" * 50)

jumlah_potongan = int(input("Masukkan Banyak Jenis Potongan Yang Ingin Dibeli : "))
# Kasih Validasi Kalo Input Nya 0
if jumlah_potongan <= 0:
    print("Jumlah jenis potongan tidak valid!")
else:
    # Inisialisasi Variabel
    data = []
    totalbayar = 0
    
    # Perulangan
    for i in range(jumlah_potongan):
        jenis = input("Masukkan Jenis Potongan : ").upper()
        banyak = int(input("Masukkan Jumlah Potongan : "))
        if jenis == "D":
            JenisPotongan = "Dada"
            harga = 2500
        elif jenis == "P":
            JenisPotongan = "Paha"
            harga = 2000
        elif jenis == "S":
            JenisPotongan = "Sayap"
            harga = 1500
        else:
            JenisPotongan = "Tidak Ada"
            harga = 0
            
        # Menghitung Jumlah Bayar
        jumlahbayar = harga * banyak
        totalbayar += jumlahbayar
        
        # Menambahkan data ke dalam list
        data.append([i+1, JenisPotongan, harga, banyak, jumlahbayar])

print("\nGEROBAK FRIED CHICKEN")
print("-" * 50)
print("No. JenisPotongan HargaSatuan BanyakBeli JumlahHarga")
print("-" * 50)

# Cetak Data
for d in data:
    no, JenisPotongan, harga, banyak, jumlahbayar = d
    print(f"{no:<5}{JenisPotongan:<15}{format_rupiah(harga):<10}{banyak:<10}{format_rupiah(jumlahbayar):<10}")
    
print("-" * 50)
# Hitung Total Bayar, Pajak, dan Total Akhir
pajak = totalbayar * 0.1
totalakhir = totalbayar + pajak

# Cetak Total Bayar, Pajak, dan Total Akhir
print(f"Total Bayar : {format_rupiah(totalbayar)}")
print(f"Pajak : {format_rupiah(pajak)}")
print(f"Total Akhir : {format_rupiah(totalakhir)}")