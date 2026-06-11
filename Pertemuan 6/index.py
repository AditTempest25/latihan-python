#Latihan

list_nim=[]
list_uts=[]
list_uas=[]
list_total=[]

ulang = 2
for i in range(ulang):
    print(f"Data Ke - {i + 1}")
    
    list_nim.append(input("Masukkan NIM : "))
    list_uts.append(int(input("Masukkan Nilai UTS : ")))
    list_uas.append(int(input("Masukkan Nilai UAS : ")))

for i in range(ulang):
    list_total.append((list_uas[i] + list_uts[i]) / 2)    

print("=============================================================")
print("Nim  Nilai Uts   Nilai UAS   Total")
print("=============================================================")
for i in range(ulang):
    print(f"{list_nim[i]:<7} {list_uts[i]:<7} {list_uas[i]:<13} {list_total[i]:<15}")
print("=============================================================")
