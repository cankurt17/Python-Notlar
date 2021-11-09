print("""
**************************
Mükemmel sayı

Çıkmak için * basınız
**************************
""")
toplam = 0
while True:
    sayi =  input("Bir sayi giriniz: ")
    if sayi == "*":
        print("Çıkış yapıldı.")
        break
    üs =len(sayi)
    for i in sayi:
        i = int(i)
        toplam += i**üs
    if int(sayi) == toplam:
        print(sayi,"armstrong sayıdır")
    else:
        print(sayi,"armstrong sayı değildir")
    toplam =0


