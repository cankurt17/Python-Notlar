

def birinci_yol():
    harfler=""
    with open("şiir.txt", "r", encoding="utf-8")as file:
        for satır in file:
            satır=satır.strip()
            harfler += satır[0]
        print(harfler)

def ikinci_yol():

    with open("şiir.txt","r",encoding="utf-8")as file:

        metin=file.read()
        satırlar = metin.split("\n")
        harfler=list()
        s =str()
        for i in satırlar:
            i=i.strip()
            harfler.append(i[0])
        for i in harfler:
            s +=i
        print(s)

birinci_yol()