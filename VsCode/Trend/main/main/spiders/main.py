import scrapy  
from ..items import trendyolItem
import pandas as pd

class QuotesSpider(scrapy.Spider):
    name = "quotes"  
 
    url="https://www.trendyol.com"
    top=list() 
    start_urls = [
        'https://www.trendyol.com/telefon?siralama=4', 
    ]  
 
    marka_list  = list()
    isim_list  = list()
    fiyat_list  = list()
    dgr_list  = list()
    puan_list  = list()
    yorum_list  = list()  


    def parse(self, response):  
        self.urls = response.css("div.p-card-chldrn-cntnr a::attr(href)").getall()   
        for i in self.urls[0:10]:
            urun,butik=i.split("?")
            self.top.append(self.url+urun+"/yorumlar")

        self.toplam=0
        yield scrapy.Request(self.top[self.toplam],callback=self.urunler) 

    def urunler(self,response):    
        items = trendyolItem()
        # Marka         :  response.css("span.product-brand::text").get()
        # İsim          :  response.css("span.product-name::text").get()
        # Fiyat         :  response.css("span.prc-slg::text").get()
        # Degerlendirme :  response.css("div.pr-rnr-sm-p-s span::text").getall()[0].split()[0]
        # Puan          :  response.css("div.pr-rnr-sm-p span::text").get()
        # Yorum         :  response.css("div.pr-rnr-sm-p-s span::text").getall()[1].split()[0]
        
        marka = response.css("span.product-brand::text").get()
        isim = response.css("span.product-name::text").get()
        fiyat = response.css("span.prc-slg::text").get().replace(",",".")

        try: 
            degerlendirme = response.css("div.pr-rnr-sm-p-s span::text").getall()[0].split()[0].replace(",",".")
            puan = response.css("div.pr-rnr-sm-p span::text").get().replace(",",".")
            yorum = response.css("div.pr-rnr-sm-p-s span::text").getall()[1].split()[0]
        except:
            degerlendirme = 0
            puan = 0
            yorum = 0
 

        self.marka_list.append(marka)
        self.isim_list.append(isim)
        self.fiyat_list.append(fiyat)
        self.dgr_list.append(degerlendirme)
        self.puan_list.append(puan)
        self.yorum_list.append(yorum)
 
        if self.toplam <9:
            self.toplam +=1
            print("************************************************************************")
            print("************************************************************************")
            print("************************************************************************")
            yield scrapy.Request(self.top[self.toplam],callback=self.urunler)
        else: 
            
            items['marka'] = self.marka_list      
            items['isim'] = self.isim_list
            items['fiyat'] = self.fiyat_list
            items['degerlendirme'] = self.dgr_list
            items['puan'] = self.puan_list
            items['yorum'] = self.yorum_list

        with open("urunler.csv","w",encoding="UTF-8")as file:
            for i,j in items.items():
                file.write(i+",")
            file.write("\n")   

            for i in range(0, 10):
                for key,value in items.items():
                    file.write(value[i]+",")
                file.write("\n")
        
        

