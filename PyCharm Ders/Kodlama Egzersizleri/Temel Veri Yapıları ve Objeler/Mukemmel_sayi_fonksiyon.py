
def mukemmel(sayi):
    toplam = 0
    for i in range(1,sayi):
        if sayi%i==0:
            toplam += i
    return  toplam == sayi

while True:
    sayi=input("Sayı: ")
    if sayi =="*":
        break
    else:
        sayi = int(sayi)
        if mukemmel(sayi):
            print(sayi,"mukemmel sayıdır")
        else:
            print(sayi, "mukemmel sayı değildir")