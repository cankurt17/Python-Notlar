
print("""
*****************************
En Büyük Sayı
*****************************1
""")

a = int(input("Birinci sayı:"))
b = int(input("İkinci sayı:"))
c = int(input("Üçüncü sayı:"))

if a>b:
    if a>c:
        print("En büyük sayı : {}".format(a))
    else:
        print("En büyük sayı : {}".format(c))
else:
    if b > c:
        print("En büyük sayı : {}".format(b))
    else:
        print("En büyük sayı : {}".format(c))