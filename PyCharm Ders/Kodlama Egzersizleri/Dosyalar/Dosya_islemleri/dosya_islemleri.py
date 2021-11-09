

class Dosya():

    def __init__(self):

        with open("metin.txt","r",encoding="utf-8")as file:
            metin = file.read()
            kelimeler = metin.split()
            self.sadece_kelimeler = list()
            self.kelimeler_kumesi = set()
            for i in kelimeler:
                i=i.strip("\n")
                i=i.strip(" ")
                i=i.strip(".")
                i=i.strip(",")
                self.sadece_kelimeler.append(i)

            for i in self.sadece_kelimeler:
                self.kelimeler_kumesi.add(i)

    def tum_kelimeler(self):

        for i in self.kelimeler_kumesi:
            print(i)
            print("****************************")

    def kelime_frekansı(self):
        frekans=list()
        for i in self.kelimeler_kumesi:
            key=self.sadece_kelimeler.count(i)

            print(str(i)+"   "+str(key))
    def kelime_frekansı2(self):
        frekans=dict()
        for i in self.sadece_kelimeler:
            if i in frekans:
                frekans[i]+=1
            else:
                frekans[i]=1
        for kelime,adet in frekans.items():
            print(str(kelime)+"   "+str(adet))
    def kelime_ara(self,kelime):
        if kelime in self.sadece_kelimeler:
            print("{}  {} adet bulunuyor".format(kelime,self.sadece_kelimeler.count(kelime)))
        else:
            print("Kelime bulunamadı")


dosya = Dosya()


while True:
    kelime = input("Kelime giriniz: ")
    if kelime=="*":
        print("Çıkılıyor")
        break
    else:
        dosya.kelime_ara(kelime)