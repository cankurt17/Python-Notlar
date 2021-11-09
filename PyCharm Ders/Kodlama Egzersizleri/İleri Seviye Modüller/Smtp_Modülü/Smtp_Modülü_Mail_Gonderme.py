


import  smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

# Tarayıcı güvenli kaynakları açmayı unutma

mesaj = MIMEMultipart()

mesaj["From"]="bencankurt17@gmail.com"
mesaj["To"]="iletisim@enlodi.com"
mesaj["Subject"]="Python mail test"

yazi="""
Python ile mail gönderiyorum
Can Kurt
"""

mesaj_govdesi=MIMEText(yazi,"plain")
mesaj.attach(mesaj_govdesi)


try:
    mail=smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("bencankurt17@gmail.com","29963207974Can.")
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
    print("Mail gönderildi.")
    mail.close()
except:
    sys.stderr.write("Bir sorun oluştu...")
    sys.stderr.flush()