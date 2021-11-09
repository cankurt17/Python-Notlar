

isim =["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisim=["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

isimsoyisim= list(zip(isim,soyisim))
isimsoyisim.sort()
for i in isimsoyisim:
    print(i[0]+" "+i[1])