

import sqlite3

con = sqlite3.connect("kütüphane.db")
cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik(İsim TEXT,Yazar TEXT,Yayinevi TEXT,Sayfa_sayisi INT)")
    con.commit()
def veri_ekle():
    cursor.execute("INSERT INTO kitaplik VALUES('Şekeroba','Can Kurt','Dedeler',21)")
    con.commit()
def veri_ekle2(isim,yazar,yayınevi,sayfa):
    cursor.execute("INSERT INTO kitaplik VALUES(?,?,?,?)",(isim,yazar,yayınevi,sayfa))
    print("Kitap eklendi...")
    con.commit()
def verileri_al():
    cursor.execute("SELECT * FROM kitaplik")
    liste=cursor.fetchall()
    print("Kitaplık tablosu: ")
    for i in liste:
        print(i)
def verileri_al2():
    cursor.execute("SELECT İsim,Sayfa_sayisi FROM kitaplik")
    liste=cursor.fetchall()
    print("Kitaplık tablosu: ")
    for i in liste:
        print(i)
def verileri_al3(yayınevi):
    cursor.execute("SELECT * FROM kitaplik WHERE Yayinevi = ?",(yayınevi,))
    liste=cursor.fetchall()
    print("Kitaplık tablosu: ")
    for i in liste:
        print(i)
def verileri_güncelle(eski_yayinevi,yeni_yayinevi):
    cursor.execute("UPDATE kitaplik SET Yayinevi=? WHERE Yayinevi=?",(yeni_yayinevi,eski_yayinevi))
    print("Kitap güncellendi...")
    con.commit()
def verileri_sil(yazar):
    cursor.execute("DELETE FROM kitaplik WHERE Yayinevi=?",(yazar,))
    

'''    
isim = input("Kitap adı: ")
yazar = input("Yazar: ")
yayınevi = input("Yayın evi: ")
sayfa = int(input("Sayfa: "))
veri_ekle2(isim,yazar,yayınevi,sayfa) 
'''
verileri_sil("maraş")
verileri_al()

con.close()
