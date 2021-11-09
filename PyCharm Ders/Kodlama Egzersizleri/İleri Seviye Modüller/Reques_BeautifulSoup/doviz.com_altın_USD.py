


import requests
from  bs4 import BeautifulSoup

url = "https://www.doviz.com/"

response = requests.get(url)
html=response.content
soup=BeautifulSoup(html,"html.parser")

kur = soup.find_all("span",{"class":"name"})
deger = soup.find_all("span",{"class":"value"})



for i,j in zip(kur,deger):
    print(i.text+" : "+j.text)


