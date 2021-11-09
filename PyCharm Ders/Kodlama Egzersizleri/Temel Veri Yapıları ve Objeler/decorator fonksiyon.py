
def mukemmel(func):

    def wrapper(sayı):
        mukemmel_sayilar = list()
        print("Mükemmel sayılar: ")
        for i in sayı:
            toplam = 0
            for j in range(1,i):
                if i%j == 0:
                    toplam += j
            if toplam==i:
                print(i)
        func(sayı)
    return wrapper
@mukemmel
def asal(sayi):
    asal_sayilar=list()
    print("Asal sayılar: ")
    for i in sayi:
        say = 0
        if i==1:
            pass
        elif i==2:
            asal_sayilar.append(i)
        else:
            for j in range(2,i):
                if i%j==0:
                    say+=1
            if say == 0:
                asal_sayilar.append(i)

    for i in asal_sayilar:
        print(i)

asal(range(1,1001))
