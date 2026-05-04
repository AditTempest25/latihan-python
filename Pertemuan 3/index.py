#String
print("=+=+=+=+ String =+=+=+=+")
var1 = "Hello World"
var2 = "I Love Python"
var3 = "I Hate Java"

print(var1)
print(var2)
print(var3)

#Mengakses Nilai String
print("=+=+=+=+ Mengakses Nilai String =+=+=+=+")
print("var1[0] = ", var1[0])
print("var2[2:6] = ", var2[2:6])

#Update String
print("=+=+=+=+ Update String =+=+=+=+")
var1 = "Hello Python"
var2 = var1[:6]
print(var1)
print("string update :", var1[:6] + "World")

#Menggabung String
print("=+=+=+=+ Menggabung String =+=+=+=+")
var1 = "Hello"
var2 = "Python"
var3 = var1 + " " + var2
print(var3)

#Menghitung Panjang String
print("=+=+=+=+ Menghitung Panjang String =+=+=+=+")
var1 = "I Miss Her"
print(len(var1))

#Karakter Escape
print("=+=+=+=+ Karakter Escape =+=+=+=+")
var1 = "I\'m a student"
print(var1)

#Raw String
print("=+=+=+=+ Raw String =+=+=+=+")
print("Hello \n World")
print(r"Hello \n World")

#Mengatur Format String
print("=+=+=+=+ Mengatur Format String =+=+=+=+")
default_order = "{0} {1} {2}".format("a", "b", "c")
print("Default order : ", default_order)

custom_order = "{2} {0} {1}".format("a", "b", "c")
print("Custom order : ", custom_order)

#Meratakan String
print("=+=+=+=+ Meratakan String =+=+=+=+")
print("|{:<10}|{:^10}|{:>10}|".format("left", "right", "center"))

#Pembulatan
print("=+=+=+=+ Pembulatan =+=+=+=+")
print("{:,.2f}".format(1234.5678))

#Format Float
print("=+=+=+=+ Format Float =+=+=+=+")
print("Format exponsional : {0:e}".format(1234.5678))

#Upper, Lower, Join, Split, Startswith, Endswith, Replace
print("=+=+=+=+ Upper, Lower, Join, Split, Startswith, Endswith, Replace =+=+=+=+")
print("Hello World".upper())
print("Hello World".lower())
print(",".join(["a", "b", "c"]))
print("a,b,c".split(","))
print("Hello World".startswith("Hello"))
print("Hello World".endswith("World"))
print("Hello World".replace("Hello", "Hi"))

#Konversi Jenis Bilangan
print("=+=+=+=+ Konversi Jenis Bilangan =+=+=+=+")
print(float("123"))
print(int(123.456))

#Phyton Decimal
print("=+=+=+=+ Phyton Decimal =+=+=+=+")
print(1.1 + 2.2)

