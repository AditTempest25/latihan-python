import penggunaan_modul
from math import *
from math import factorial
# Bisa pakai alias (as) juga untuk mempersingkat, misal import penggunaan_modul as pm

print(penggunaan_modul.penjumlahan(5, 3))

# Contoh Penggunaan Sebagian fungsi Modul
bil = int(input("Masukkan bilangan: "))
faktorial = factorial(bil)
print(f"Faktorial dari {bil} adalah {faktorial}")

# Contoh Penggunaan Semua Fungsi pada Suatu Modul
pangkat = pow(2, 3)
print(f"hasil dari pemangkatan bilangan adalah {pangkat}")
