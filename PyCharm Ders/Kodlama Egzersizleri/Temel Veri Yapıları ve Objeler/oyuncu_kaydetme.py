print("Oyuncu Kaydetme Programı")


ad = input("Oyuncunun adı:")
soyad = input("Oyuncunun soyadı:")
takım = input("Oyuncunun takımı:")

bilgiler = [ad,soyad,takım]

print("Bilgiler kaydediliyor...")

print("Oyuncunun adı: {}\nOyuncunun soyadı: {}\nOyuncunun takımı: {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("Bilgiler kaydedildi...")