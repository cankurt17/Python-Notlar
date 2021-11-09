
print("""
**************************
Kullanıcı Girişi
**************************
""")

sys_kulllanıcı_adı = "cankurt"
sys_parola = "1"
giris = 3

while True:

    kullanıcı_adı = input("Kullanıcı adı:")
    parola = input("Parola:")

    if kullanıcı_adı == sys_kulllanıcı_adı and parola !=sys_parola:
        giris -=1
        print("Parola Hatalı")
    elif kullanıcı_adı != sys_kulllanıcı_adı and parola == sys_parola:
        giris -= 1
        print("Kullanıcı adı Hatalı")
    elif kullanıcı_adı != sys_kulllanıcı_adı and parola != sys_parola:
        giris -= 1
        print("Kullanıcı adı  ve Parola Hatalı")
    else:
        print("Giriş Başarılı...")
        break
    if giris ==0:
        print("Giriş hakkınız bitti.")
        break