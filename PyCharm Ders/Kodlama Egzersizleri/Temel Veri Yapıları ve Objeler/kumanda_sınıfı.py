import random
import  time

class Kumanda():

    def __init__(self,durum="",ses=0,kanallar=["trt"],kanal= ""):

        self.durum = durum
        self.ses = ses
        self.kanallar = kanallar
        self.kanal = kanal

    def tvAc(self):
        if self.durum=="Açık":
            print("Televizyon zaten açık")
        else:
            print("Televizyon açılıyor...")
            self.durum = "Açık"
    def tvKapat(self):
        if self.durum=="Kapalı":
            print("Televizyon zaten kapalı")
        else:
            print("Televizyon kapatılıyor...")
            self.durum = "Kapalı"
    def sesAyarı(self):
        while True:
            cevap = input("1.Arrıtmak için +\n2.Azaltmak için - \n3.Çıkmak için * \nGiriş: ")
            if cevap == "-":
                if self.ses != 0:
                    self.ses -=1
                    print("Ses: ",self.ses)
            elif cevap == "+":
                if self.ses !=30:
                    self.ses += 1
                    print("Ses: ",self.ses)
            else:
                print("Ses güncellendi: ",self.ses)
                break
    def kanalEkle(self,kanal):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanallar.append(kanal)
        print("Kanal eklendi.")
    def rasgeleKanal(self):
        rastgele = random.randint(0,len(self.kanallar)-1)
        self.kanal = self.kanallar[rastgele]
        print("Şuanki kanal: ",self.kanal)
    def __len__(self):
        return len(self.kanallar)
    def __str__(self):
        return """
                Tv durumu: {}
                Tv ses: {}
                Tv kanal listesi: {}
                Tv kanal: {}
        """.format(self.durum,self.ses,self.kanallar,self.kanal)


print("""

    Tv Uygulaması

    1.Tv Aç
    2.Tv Kapat
    3.Ses Ayarları
    4.Kanal Ekle
    5.Kanal sayısı
    6.Rastgele Kanal
    7.Televizyon bilgileri
    8.Kumanda Ekle
    9.Kumanda Sil
    
    Çıkmak için * basınız.

    """)

kumanda = Kumanda()
while True:
    işlem = input("İşlem seçiniz: ")
    if işlem == "*":
        print("Uygulama kapatıldı")
        break
    elif işlem == "1":
        kumanda.tvAc()
    elif işlem == "2":
        kumanda.tvKapat()
    elif işlem=="3":
        kumanda.sesAyarı()
    elif işlem=="4":
        kanal_isimleri=input("Kanal isimlerini , ile ayırarak yazınız: ")
        kanal_listesi = kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanalEkle(eklenecekler)
    elif işlem =="5":
        print("Kanal sayısı: ",len(kumanda))
    elif işlem =="6":
        kumanda.rasgeleKanal()
    elif işlem == "7":
        print(kumanda)
    else:
        print("Geçersiz işlem....")

