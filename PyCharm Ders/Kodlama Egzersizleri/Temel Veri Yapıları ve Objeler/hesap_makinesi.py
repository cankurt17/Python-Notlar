

print("""
*********************** 
İşlemler: 
1.Toplama 
2.Çıkarma
3.Çarpma
4.Bölme 
*********************** 
""")

a = int(input("Birinci sayı:"))
b = int(input("İkinci sayı:"))

islem = int(input("İşlem seçiniz:"))

if islem==1:
    print("{} ile {} nin toplamı {} dır".format(a,b,a+b))
elif islem==2:
    print("{} ile {} nin farkı {} dır".format(a,b,a-b))
elif islem==3:
    print("{} ile {} nin çarpımı {} dır".format(a,b,a*b))
elif islem==4:
    print("{} ile {} nin bö2lümü {} dır".format(a,b,a/b))
else:
    print("Geçersiz işlem...")
