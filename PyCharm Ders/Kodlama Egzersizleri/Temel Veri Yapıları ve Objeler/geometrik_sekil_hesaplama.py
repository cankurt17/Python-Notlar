


print("""
************************** 
Geometrik Şekil Hesaplama
**************************
""")

kenar = input("Geometrik şekli belirtiniz(Üçgen/Dörtgen):")

if kenar == "Dörtgen":
    a = input("Birinci kenar:")
    b = input("İkinci kenar:")
    c = input("Üçüncü kenar:")
    d = input("Dördüncü kenar:")

    if a==b==c==d:
        print("Geometrik şekil kare.")
    elif (a==b and c==d) or (a==c and b==d) or (a==d and b==c):
        print("Geometrik şekil dikdörtgen.")
    else:
        print("Geometrik şekil dörtgen.")

elif kenar == "Üçgen":
    a = int(input("Birinci kenar:"))
    b = int(input("İkinci kenar:"))
    c = int(input("Üçüncü kenar:"))

    if ( abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):

        if a==b==c:
            print("Eşkenar üçgen.")
        elif a==b or a==c or b==c:
            print("İkizkenar üçgen.")
        else:
            print("Çeşitkenar üçgen.")
    else:
        print("üçgen belirtmiyor")
else:
    print("Geçersiz şekil.")