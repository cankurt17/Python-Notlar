

import os
from datetime import datetime
'''
-----------dosyayı dizine taşır
os.chdir("C:/Users/benca/OneDrive/Masaüstü/Python/PyCharm Ders/Kodlama Egzersizleri/İleri Seviye Modüller")

-----------dosya yolunu dönderir
print(os.getcwd())
 
-----------Bulunduğu dizideki dosyaları dönderir
for i in os.listdir():
    print(i)

----------dizine dosya açar o dizin yoksa hata verir
os.mkdir("test") ----True
os.mkdir("test2/test3")----False

----------dizine dosya açar o dizin yoksa dizini açar
os.makedirs("test2/test3")

----------dizindeki dosyayı siler fakat alt klasörleri silmez
os.rmdir("test2/test3")

----------dizindeki bütün dosyaları siler alt klasörlerle birlikte
os.removedirs("test2/test3")

----------dosyanın adını değiştirir
os.rename("text.txt","test2.txt")

----------dosya özelliklerini döner
print(os.stat("test2.txt"))
print(datetime.fromtimestamp(os.stat("test2.txt").st_mtime))

----------Dizin altındaki bütün klasör özelliklerini döner
for i in  os.walk("C:/Users/benca/OneDrive/Masaüstü"):
    print(i)
for dizin,klasör_isim,dosya_isim in os.walk("C:/Users/benca/OneDrive/Masaüstü"):
    print("Dizi: ",dizin)
    print("Klasör isimleri: ",klasör_isim)
    print("Dosya isimleri: ",dosya_isim)
    print("******************************")
    
----------sadece text dosyalarını döderir
for dizin,klasör_isim,dosya_isim in os.walk("C:/Users/benca/OneDrive/Masaüstü"):
    for i in dosya_isim:
        if i.endswith(".txt"):
            print(i)
'''






