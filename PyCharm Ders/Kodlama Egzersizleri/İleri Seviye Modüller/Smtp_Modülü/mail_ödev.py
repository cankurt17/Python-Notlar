


import smtplib
from  email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()
yazı = "Bu bir test mailidir"
mesaj_govdesi = MIMEText(yazı, "plain")

liste = list()
with open("mailler.txt","r",encoding="utf-8")as  file:
    for i in file.readlines():
        i=str(i)
        i = i.strip("\n")
        i=i.split(",")

        mesaj = MIMEMultipart()
        mesaj.attach(mesaj_govdesi)

        mesaj["From"] = "bencankurt17@gmail.com"
        mesaj["Subject"] = i[0]
        mesaj["To"] = i[1]

        try:
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login("bencankurt17@gmail.com", "29963207974Can.")
            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
            print("Mail gönderildi.")
            mail.close()
        except:
            sys.stderr.write("Bir sorun oluştu...")
            sys.stderr.flush()
