print("""
**************************
While dongüsü

Çıkmak için * basınız
**************************
""")

toplam = 0

while True:
    a = input("Bir sayı giriniz: ")
    if a == "*":
        print("Toplam : ",toplam)
        break
    toplam += int(a)
