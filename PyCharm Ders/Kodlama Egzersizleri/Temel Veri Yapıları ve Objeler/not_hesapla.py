
gecenler=[]
kalanlar=[]

def sonuc(isim,sonuc):
    if sonuc=="FF":
        kalanlar.append(isim+"\n")
    else:
        gecenler.append(isim+"\n")


def not_hesapla(satır):

    satır = satır[:-1]
    liste = satır.split(",")
    isim = liste[0]
    not1=int(liste[1])
    not2=int(liste[2])
    not3=int(liste[3])

    ort = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if ort >= 90:
        harf = "AA"
    elif ort >= 85:
        harf = "BA"
    elif ort >=80:
        harf = "BB"
    elif ort >=75:
        harf = "CB"
    elif ort >= 70:
        harf = "CC"
    elif ort >= 65:
        harf = "DC"
    elif ort >= 60:
        harf = "DD"
    elif ort >= 55:
        harf = "FD"
    else:
        harf="FF"
    sonuc(isim,harf)
    return isim + "--------------->  " + harf +"\n"

with open("C:/Users/benca/OneDrive/Masaüstü/Python/PyCharm Ders/Kodlama Egzersizleri/Dosyalar/not_hesapla/dosya.txt", "r", encoding="utf-8") as file:

    eklenecekler_listesi=[]
    for i in file:
        eklenecekler_listesi.append(not_hesapla(i))

    with open("C:/Users/benca/OneDrive/Masaüstü/Python/PyCharm Ders/Kodlama Egzersizleri/Dosyalar/not_hesapla/notlar.txt", "w", encoding="utf-8") as file2:
        file2.writelines(eklenecekler_listesi)

    with open("C:/Users/benca/OneDrive/Masaüstü/Python/PyCharm Ders/Kodlama Egzersizleri/Dosyalar/not_hesapla/geçenler.txt", "w", encoding="utf-8") as file3:
        file3.writelines(gecenler)

    with open("C:/Users/benca/OneDrive/Masaüstü/Python/PyCharm Ders/Kodlama Egzersizleri/Dosyalar/not_hesapla/kalanlar.txt", "w", encoding="utf-8") as file4:
        file4.writelines(kalanlar)