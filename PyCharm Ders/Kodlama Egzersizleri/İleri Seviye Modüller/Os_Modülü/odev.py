

import  os


for dizin,klasör_isim,dosya_isim in os.walk("C:/Users/benca/OneDrive/Masaüstü"):
    for i in dosya_isim:
        if i.endswith(".txt"):
            with open("txt_dosyaları.txt","a",encoding="utf-8") as file:
                file.write(i+"----------------------"+dizin+"\n")
        elif i.endswith(".mp3"):
            with open("mp3_dosyaları.txt", "a", encoding="utf-8") as file:
                file.write(i + "----------------------" + dizin + "\n")
        elif i.endswith(".pdf"):
            with open("pdf_dosyalari.txt", "a", encoding="utf-8") as file:
                file.write(i + "----------------------" + dizin + "\n")
