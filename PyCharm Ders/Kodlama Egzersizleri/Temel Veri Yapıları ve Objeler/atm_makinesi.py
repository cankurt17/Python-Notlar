

print("""
**************************
    ATM'ye Hoşgeldiniz.
**************************

İşlemler:

1.Bakiye Sorgulama
2.Para Yatırma
3.Para Çekme

Programdan çıkmak için * basınız.
""")
bakiye = 1000
while True:
    işlem = input("İşlem seçiniz:")

    if işlem == "*":
        print("Çıkış yapıldı...")
    elif işlem =="1":
        print("Bakiyeniz: {} TL".format(bakiye))
    elif işlem =="2":
        miktar = int(input("Miktarı giriniz:"))
        bakiye += miktar
    elif işlem =="3":
        miktar = int(input("Çekilecek miktarı giriniz:"))
        if bakiye - miktar <0:
            print("Yetersiz bakiye")
            continue
        bakiye -= miktar
    else:
        print("Yanlış işlem seçtiniz...")

