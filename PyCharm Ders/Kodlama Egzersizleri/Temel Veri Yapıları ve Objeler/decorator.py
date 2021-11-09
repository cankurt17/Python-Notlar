
def ekstra(fonk):
    def wrapper(sayılar):
        çiftler_toplamı=0
        çift_sayılar=0
        tekler_toplamı=0
        tek_sayılar=0

        for i in sayılar:
            if i % 2 ==0:
                çift_sayılar +=1
                çiftler_toplamı +=i
            else:
                tek_sayılar +=1
                tekler_toplamı+=i
        print("Teklerin ortalaması: ",tekler_toplamı/tek_sayılar)
        print("Çiftlerin ortalaması",çiftler_toplamı/çift_sayılar)
        fonk(sayılar)
    return  wrapper

@ekstra
def ortalama(sayı):
    toplam=0
    for i in sayı:
        toplam += i
    print("Ortalama: ",toplam/len(sayı))

ortalama([1,2,3,4,5,6])


