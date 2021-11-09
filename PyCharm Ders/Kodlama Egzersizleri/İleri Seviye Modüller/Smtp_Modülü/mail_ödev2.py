import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

with open("mailler.txt", "r", encoding="utf-8") as mailler:
    list1 = mailler.readlines()
    mailler.close()

list2 = list()

for i in list1:
    i = str(i)
    i = i.strip("\n")
    i = i.split(",")
    i = list2.append(i)

mesaj = MIMEMultipart()

for isim, mail in list2:
    mesaj = MIMEMultipart()

    mesaj["From"] = "bencankurt17@gmail.com"

    mesaj["To"] = mail

    mesaj["Subject"] = "Proje icin mail denemesi PYTHON"

    yazi = """
    Sayin {} ,
    Bu mail bir proje denemesidir.
    ----------PYTHON Ile Gonderildi-----------
    """.format(isim)

    mesaj_govdesi = MIMEText(yazi, "plain")

    mesaj.attach(mesaj_govdesi)

    try:
        mail = smtplib.SMTP("smtp.gmail.com", 587)

        mail.ehlo()

        mail.starttls()

        mail.login("bencankurt17@gmail.com", "29963207974Can.")

        mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())

        print("Mesaj basariyla gonderildi...")

        mail.close()

    except:
        sys.stderr.write("Uppssss... Bir sorunumuz var !!!")
        sys.stderr.flush()