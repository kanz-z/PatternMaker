def intro():
    print("Halo! Mau buat apa nih?")
    mulai()

def mulai():
    print("1. Buat piramida!")
    print("2. Buat segitiga siku-siku! (kiri)")
    print("3. Buat segitiga siku-siku! (kanan)")
    print("4. Buat belah ketupat!")
    print("0. Enggak jadi.")
    while True:
        try:
            masukan = int(input("Masukkan angka: "))
            break
        except ValueError:
            print("Input salah. Masukkan angka saja.")
    if masukan == 1:
        pyramid()
    elif masukan == 2:
        segitiga_kiri()
    elif masukan == 3:
        segitiga_kanan()
    elif masukan == 4:
        belah_ketupat()
    elif masukan == 0:
        return
    else:
        print("Tidak ada dalam pilihan.")

def pyramid():
    while True:
        try:
            x = int(input("Tinggi piramida: "))
            break
        except ValueError:
            print("Input salah. Masukkan angka saja.")
    for i in range(1, x+1):
        spasi = x - i
        print(" " * spasi + "*" * (2*i-1))
    kelanjutan()

def segitiga_kiri():
    while True:
        try:
            x = int(input("Tinggi segitiga siku kiri: "))
            break
        except ValueError:
            print("Input salah. Masukkan angka saja.")
    for i in range(1, x+1):
        spasi = x - i
        print("*" * i)
    kelanjutan()

def segitiga_kanan():
    while True:
        try:
            x = int(input("Tinggi segitiga siku kanan: "))
            break
        except ValueError:
            print("Input salah. Masukkan angka saja.")
    for i in range(1, x+1):
        spasi = x - i
        print(" " * spasi + "*" * i)
    kelanjutan()

def belah_ketupat():
    while True:
        try:
            x = int(input("Tinggi piramida: "))
            break
        except ValueError:
            print("Input salah. Masukkan angka saja.")
    for i in range(1, x+1):
        spasi = x - i
        print(" " * spasi + "*" * (2*i-1))
    for i in range(x-1, 0, -1):
        spasi = x - i
        print(" " * spasi + "*" * (2*i-1))
    kelanjutan()

def kelanjutan():
    i = str(input("Mau buat yang lain? (y/n): "))
    if i == "y":
        mulai()
    elif i == "n":
        return
    else:
        print("Error: Masukkin 'y' atau 'n' njir. Bukan lainnya.")
intro()

#     * 
#    * * 
#   * * *
#  * * * *
# * * * * *
#
#
#
#  *
# ***
#*****
