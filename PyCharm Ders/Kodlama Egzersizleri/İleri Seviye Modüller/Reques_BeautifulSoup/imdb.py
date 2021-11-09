



import requests
from  bs4 import  BeautifulSoup

url="https://www.imdb.com/chart/top"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html,"html.parser")


a = float(input("Ratingi giriniz: "))

basliklar = soup.find_all("td",{"class":"titleColumn"})

ratingler = soup.find_all("td",{"class":"ratingColumn imdbRating"})

for baslik,rating in zip(basliklar,ratingler):

      baslik = baslik.text
      rating = rating.text

      baslik=baslik.strip()
      baslik=baslik.replace("\n","")
      rating = rating.strip()
      rating = rating.replace("\n","")

      if(float(rating)>a):
          print("Film ismi : {}  IMDB: {}".format(baslik,rating))



