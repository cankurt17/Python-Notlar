


with open("mailler.txt","r",encoding="utf-8")as file:

    for satır in file:
        satır= satır.strip("\n")
        satır= satır.strip()
        if satır.endswith(".com") and satır.count("@")==1:
            print(satır)
