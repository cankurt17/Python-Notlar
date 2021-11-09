

import requests
from  bs4 import BeautifulSoup


url="https://www.trendyol.com/tws/airpods-i12-beyaz-iphone-android-universal-bluetooth-kulaklik-hd-ses-kalitesi-p-31511124?boutiqueId=340395&merchantId=123868"
response = requests.get(url)

html_icerigi=response.content
soup = BeautifulSoup(html_icerigi,"html.parser")

"""
-----------Html içeriğini dönderir
print(soup.prettify())

-------------------------seçili başlıkları dönderir
for i in soup.find_all("a"):
    #print(i.get("href"))
    print(i.text)
    print("**************************************")
"""

print(soup.find_all("div",{"class":"caption"}))


