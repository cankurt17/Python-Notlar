

print("""
**************************
Kullanıcı Girişi
**************************
""")

sys_kulllanıcı_adı = "cankurt"
sys_parola="1"

kullanıcı_adı = input("Kullanıcı adı:")
parola = input("Parola:")

if kullanıcı_adı == sys_kulllanıcı_adı and parola !=sys_parola:
    print("Parola Hatalı")
elif kullanıcı_adı != sys_kulllanıcı_adı and parola == sys_parola:
    print("Kullanıcı adı Hatalı")
elif kullanıcı_adı != sys_kulllanıcı_adı and parola != sys_parola:
    print("Kullanıcı adı  ve Parola Hatalı")
else:
    print("Giriş Başarılı...")
