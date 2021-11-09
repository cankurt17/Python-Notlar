


from  datetime import  datetime
import locale
locale.setlocale(locale.LC_ALL,"")
zaman = datetime.now()
'''

print(zaman.year)
print(zaman.month)
print(zaman.day)
print(zaman.hour)

print(datetime.ctime(zaman)) 

print(datetime.strftime(zaman,"%Y"))
print(datetime.strftime(zaman,"%B"))
print(datetime.strftime(zaman,"%D"))
print(datetime.strftime(zaman,"%A"))
print(datetime.strftime(zaman,"%Y %B ")) 
print(datetime.strftime(zaman,"%Y %B "))


saniye = datetime.timestamp(zaman)
print(saniye) 
saniye2=datetime.fromtimestamp(saniye)
print(saniye2)

-----------eppok time

'''

tarih = datetime(2023,12,1)
zaman = datetime.now()
print(tarih-zaman)
