

import  sys

"""

a= int(input("a:"))
b= int(input("b:")) 
sys.exit() 
b= int(input("c:"))

sys.stderr.write("BU bir  hata mesajıdır\n")
sys.stderr.flush()  
sys.stdout.write("Bu normal yazıdır")

print(sys.argv)
for i in sys.argv:
    print(i)
"""

"""
-------(venv) C:\Users\benca\OneDrive\Masaüstü\Python\PyCharm Ders\Kodlama Egzersizleri\İleri Seviye Modüller>python Sys_Modülü.py 1 2 3
-------Terminalde çalışıyor
def kok_bulma(a,b,c):
    delta = (b ** 2) - (4 * a * c)

    birinci_kok = (-b - (delta ** 0.5)) / (2 * a)
    ikinci_kok = (-b + (delta ** 0.5)) / (2 * a)

    return birinci_kok,ikinci_kok

if len(sys.argv) ==4:
    print("Kok bulma: ",kok_bulma(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
else:
    sys.stderr.write("Lütfen doğru değerler giriniz...")
    sys.stderr.flush()
"""