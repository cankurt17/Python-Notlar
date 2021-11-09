


print("""
**************************
    Faktoriyel Hesaplama
************************** 
Programdan çıkmak için * basınız.
""")

while True:
    sayi = input("Sayıyı giriniz: ")
    i = 1
    if sayi == "*":
        print("Çıkış yapıldı.")
        break
    for j in range(int(sayi),0,-1):
         i = i*j

    print("{}! = {}".format(sayi,i))