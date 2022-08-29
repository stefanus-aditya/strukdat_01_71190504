print("pilih menu")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

while(True):
    pilih =int( input("Pilih Bilangan "))
    a = int(input("bilangan pertama "))
    b = int(input("bilangan kedua "))
    if pilih == 1:
        print(a + b)
    if pilih == 2:
        print(a - b)
    if pilih == 3:
        print(a * b)
    if pilih == 4:
        print(a / b)
    stop = input("ketik Q jika anda ingin berhenti" )
    if stop == ("q") or ("Q"):
        break
 

