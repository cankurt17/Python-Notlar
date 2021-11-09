

import random
import time

print("""
**************************
    Sayı Tahmini
**************************
 
 1 ile 40 arasında sayıyı tahmin ediniz.
""")

random = random.randint(1,40)
tahmin_hakkı = 7
while True:
    tahmin = int(input("Tahmin: "))

    if tahmin < random:
        print("Sorgulanıyor")
        time.sleep(1)
        print("Daha yüksek")
        tahmin_hakkı -=1
        print("Kalan hakkınız: ",tahmin_hakkı)
    elif tahmin > random:
        print("Sorgulanıyor")
        time.sleep(1)
        print("Daha düşük")
        tahmin_hakkı -= 1
        print("Kalan hakkınız: ", tahmin_hakkı)
    else:
        print("Sorgulanıyor")
        time.sleep(1)
        print("Tebrikler! Sayımız ",random)
        break
    if tahmin_hakkı == 0:
        print("Hakkınız bitti...Kaybettiniz...")
        print("Sayımız: ",random)
        break