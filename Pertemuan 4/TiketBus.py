def format_rupiah(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")

print("=== PENJUALAN TIKET BUS ===")

nama = input("Nama Pembeli : ")

while True:
    no_hp = input("No Handphone : ")
    if no_hp.isdigit():
        break
    else:
        print("Input harus angka, coba lagi!")

jurusan = input("Pilih Tujuan Keberangkatan [SBY/BL/JKT] : ").upper()

if jurusan == "SBY":
    namajurusan = "Surabaya"
    harga = 500000
elif jurusan == "BL":
    namajurusan = "Bali"
    harga = 700000
elif jurusan == "JKT":
    namajurusan = "Jakarta"
    harga = 1000000
else:
    print("Jurusan tidak tersedia!")
    namajurusan = "-"
    harga = 0

while True:
    try:
        jumlah = int(input("Jumlah Penumpang : "))
        if jumlah > 0:
            break
        else:
            print("Jumlah harus lebih dari 0!")
    except:
        print("Input harus angka!")

total = harga * jumlah

# Diskon
if jumlah >= 3:
    diskon = total * 0.1
else:
    diskon = 0
total_akhir = total - diskon

# OUTPUT TOTAL
print("\n------------------------------------")
print("        RINCIAN HARGA")
print("------------------------------------")
print(f"Harga Tiket            : {format_rupiah(harga)}")
print(f"Jumlah Penumpang       : {jumlah}")
print(f"Total Harga            : {format_rupiah(total)}")
print(f"Diskon                 : {format_rupiah(diskon)}")
print(f"Total Setelah Diskon   : {format_rupiah(total_akhir)}")
print("------------------------------------")

while True:
    try:
        bayar = int(input("Uang Bayar : "))
        if bayar >= total_akhir:
            break
        else:
            print("Uang kurang! Masukkan nominal yang cukup.")
    except:
        print("Input harus angka!")

kembalian = bayar - total_akhir

# Output akhir (struk)
print("\n------------------------------------")
print("        STRUK PEMBELIAN")
print("------------------------------------")
print(f"Nama Pembeli           : {nama}")
print(f"No Handphone           : {no_hp}")
print(f"Tujuan Keberangkatan   : {namajurusan}")
print(f"Total Bayar            : {format_rupiah(total_akhir)}")
print(f"Uang Bayar             : {format_rupiah(bayar)}")
print(f"Kembalian              : {format_rupiah(kembalian)}")
print("------------------------------------")