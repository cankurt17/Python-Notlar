print("""
**************************
Mükemmel sayı

Çıkmak için 9 basınız
**************************
""")

list=list()
toplam = 0
while True:
    sayi = int(input("Bir sayi giriniz: "))
    if sayi== 9:
        print("Çıkış yapıldı.")
        break
    for i in range(1,sayi):
         if (sayi%i )==0:
             toplam += i
    if sayi == toplam:
        print(sayi,"mükemmel sayıdır")
    else:
        print(sayi,"mükemmel sayı değildir")
    toplam = 0