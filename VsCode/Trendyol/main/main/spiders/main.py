import scrapy  
from ..items import MainItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"  

    url="https://www.trendyol.com/tws/airpods-i12-beyaz-iphone-android-universal-bluetooth-kulaklik-hd-ses-kalitesi-p-31511124/yorumlar"
 
    start_urls = [
        'https://www.trendyol.com/telefon?siralama=4', 
    ]  

    def parse(self, response):  
        self.urls = response.css("div.p-card-chldrn-cntnr a::attr(href)").getall()   
        
        return scrapy.Request(self.url,callback=self.urunler) 

    def urunler(self,response):    

        items = MainItem()
        # Marka         :  response.css("span.product-brand::text").get()
        # İsim          :  response.css("span.product-name::text").get()
        # Fiyat         :  response.css("span.prc-slg::text").get()
        # Degerlendirme :  response.css("div.pr-rnr-sm-p-s span::text").getall()[0].split()[0]
        # Puan          :  response.css("div.pr-rnr-sm-p span::text").get()
        # Yorum         :  response.css("div.pr-rnr-sm-p-s span::text").getall()[1].split()[0]
        
        print("***********************************************************************")  
         
        marka = response.css("span.product-brand::text").get()
        isim = response.css("span.product-name::text").get()
        fiyat = response.css("span.prc-slg::text").get()
        degerlendirme = response.css("div.pr-rnr-sm-p-s span::text").getall()[0].split()[0]
        puan = response.css("div.pr-rnr-sm-p span::text").get()
        yorum = response.css("div.pr-rnr-sm-p-s span::text").getall() 
