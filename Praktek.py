#Mencetak Menu
import math
def menu():
    print("Pilih Bentuk 2D")
    print
    print("1. Persegi Panjang")
    print("2. Lingkaran")
    print("3. Segitiga")
    print("4. Jajar genjang")
    print("5. Trapesium")
    print("6. pythagoras")
    print("7. Keluar")

def selesai():
    print("Coba lagi [Y/N] ?")
    back = input().upper()
    if back == 'Y':
        menu()
    else:
        exit()
        
def persegi():
    print("\n"*2)
    print("Silahkan dipilih")
    print("———————————————–")
    print("1. Keliling")
    print("2. Luas")
    print("3. Luas dan Keliling")
    print("4. Kembali ke menu")
    pilih = input("Masukan pilihanmu : ")
    
    if pilih == '1':
        print("Menghitung Keliling persegi panjang")
        p = int(input("Masukkan Panjang : "))
        l = int(input("Masukkan Lebar : "))
        Keliling = 2 * ( p + l )
        print("Keliling persegi panjang adalah ", Keliling)
        selesai()
            
    elif pilih == '2':
        print("Menghitung Luas Persegi Panjang")
        p = int(input("Masukkan Panjang : "))
        l = int(input("Masukkan Lebar : "))
        luas = p * l
        print("Luas Persegi Panjang adalah ",luas)
        selesai()
            
    elif pilih == '3':
        p = int(input("Masukkan Panjang : "))
        l = int(input("Masukkan Lebar : "))
        luas = p * l
        Keliling = 2 * ( p + l )
        print("Luas Persegi Panjang adalah ",luas)
        print("Keliling persegi panjang adalah ", Keliling)
        selesai()
    elif pilih == '4':
        print("kembali ke menu")
        menu()
            
    else:
        persegi()   

def lingkaran():
    print(" Menghitung Luas Lingkaran")
    print(" dan keliling lingkaran")
    r = int(input("Masukkan Jari-Jari : "))
    if r % 7 == 0:
        Luas = (22*(r**2))/7
        keliling = (2*22*r)/7
        print("Luas Lingkaran adalah ",Luas)
        print("Keliling Lingkaran adalah ",keliling)
        
    else:
        Luas = 3.14*(r**2)
        keliling = 2*3.14*r
        print("Luas Lingkaran adalah ",Luas)
        print("Keliling Lingakaran adalah ",keliling)
    selesai()

def segitiga():
    print("Menghitung Luas Segitiga")
    a = int(input("Masukkan Alas : "))
    t = int(input("Masukkan Tinggi : "))
    luas = (a*t)/2
    print("Luas Segitiga adalah ",luas)
    selesai()
        
def jajar_genjang():
    a = int(input("masukan alas : "))
    t = int(input("masukan tinggi : "))
    Luas = (a*t)/2
    print("Luas jajar genjang adalah",Luas)
    selesai()
        
def trapesium():
    a = int(input("masukan alas bagian bawah : "))
    b = int(input("masukan alas bagian atas : "))
    t = int(input("masukan tinggi : "))
    Luas = ((a+b)*t)/2
    print("Luas trapesium adalah ",Luas)
    selesai()

def pythagoras():
    print("1.sisi miring")
    print("2.tinggi")
    print("3.alas")
    pilih = input("masukan pilihan: ")
    if pilih == '1':
        b = int(input("panjang alas: "))
        c = int(input("panjang tinggi: "))
        a = ((b*b) + (c*c))
        print("panjang sisi miring adakah",math.sqrt(a))
        selesai()
    elif pilih == '2':
        b = int(input("panjang sisi miring: "))
        c = int(input("panjang alas: "))
        a = ((b*b) - (c*c))
        print("panjang tinggi adakah",math.sqrt(a))
        selesai()
    elif pilih == '3':
        b = int(input("panjang sisi miring: "))
        c = int(input("panjang tinggi: "))
        a = ((b*b) - (c*c))
        print("panjang aaas adakah",math.sqrt(a))
        selesai()
    else:
        pytagoras()

#Program Menghitung Luas
print("      _")
print(" _ __(_)_   _  __ _ _ __")
print("| `__| | | | |/ _` | `_ \ ")
print("| |  | | |_| | (_| | | | |")
print("|_|  |_|\__, |\__,_|_| |_|")
print("        |___/")
print("Selamat Datang di Program Untuk Menghitung Luas")
print("———————————————–")
print
menu()

while 1:
#input
    pilih = input("Masukkan pilihan : ")
    if pilih == '1':
        persegi()
    
    elif pilih == '2':
        lingkaran()
    
    elif pilih == '3':
        segitiga()
    elif pilih == '4':
        jajar_genjang()
        
    elif pilih == '5':
        trapesium()
    
    elif pilih == '6':
        pythagoras()
        
    elif pilih == '7':
        print("\n"*100)
        break
    
    else:
        selesai()
