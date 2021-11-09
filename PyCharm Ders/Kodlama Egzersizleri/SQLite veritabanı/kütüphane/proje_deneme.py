from kutuphane  import*

print(
"""
**********************************
    Kütüphaneye Hoşgeldiniz...
**********************************
    İşlemler: 
    1.Kitapları Göster
    2.Kitap Sorgulama
    3.Kitap Ekle
    4.Kitap Sil
    5.Baskı Yükselt
    
    Çıkmak için * basınız...
********************************** 
""")

kütüphane = Kütüphane()

while True:
    işlem = input("İşlem seçiniz: ")
    if işlem =="*":
        print("Program sonlandırılıyor...")
        break
    elif işlem == "1":
        kütüphane.kitaplari_goster()
    elif işlem == "2":
        isim = input("Hangi kitapı istiyorsunuz: ")
        print("Kitap sorgulanıyor...")
        time.sleep(1)
        kütüphane.kitap_sorgula(isim)
    elif işlem == "3":
        isim = input("Kitap adı: ")
        yazar = input("Yazar: ")
        yayınevi = input("Yayın evi: ")
        tur=input("Tur: ")
        baski = int(input("Baskı: "))
        yeni_kitap=Kitap(isim,yazar,yayınevi,tur,baski)
        print("Kitap ekleniyor...")
        time.sleep(1)
        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi...")
    elif işlem == "4":
        isim = input("Hangi kitabı silmek istiyorsunuz: ")
        cevap = input("Eminmisiniz E/H ? ")
        if cevap =="E":
            kütüphane.kitap_sil(isim)
            print("Kitap silindi...")
    elif işlem == "5":
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz: ")
        kütüphane.baski_yuselt(isim)
    else:
        print("Geçersiz işlem...")



