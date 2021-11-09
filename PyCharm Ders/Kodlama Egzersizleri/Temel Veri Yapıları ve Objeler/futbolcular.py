
gs = []
fb = []
bjk = []

def takım(satır):
    satır = satır[:-1]
    oyuncu= satır.split(",")

    isim=oyuncu[0]
    takım=oyuncu[1]

    if takım=="Galatasaray":
        gs.append(isim+"\n")
    elif takım=="Fenerbahçe":
        fb.append(isim+"\n")
    elif takım=="Beşiktaş":
        bjk.append(isim+"\n")

with open("C:/Users/benca/OneDrive/Masaüstü/Python/PyCharm Ders/Kodlama Egzersizleri/Dosyalar/Futbolcular/futbolcular.txt","r",encoding="utf-8") as file:
    for i in file:
        takım(i)
    with open(
        "C:/Users/benca/OneDrive/Masaüstü/Python/PyCharm Ders/Kodlama Egzersizleri/Dosyalar/Futbolcular/gs.txt",
        "w", encoding="utf-8") as file2:
        file2.writelines(gs)

    with open(
        "C:/Users/benca/OneDrive/Masaüstü/Python/PyCharm Ders/Kodlama Egzersizleri/Dosyalar/Futbolcular/fb.txt",
        "w", encoding="utf-8") as file3:
        file3.writelines(fb)
    with open(
        "C:/Users/benca/OneDrive/Masaüstü/Python/PyCharm Ders/Kodlama Egzersizleri/Dosyalar/Futbolcular/bjk.txt",
        "w", encoding="utf-8") as file4:
        file4.writelines(bjk)