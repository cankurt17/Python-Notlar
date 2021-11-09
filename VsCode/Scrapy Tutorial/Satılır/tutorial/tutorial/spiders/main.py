import scrapy 
# response.css("ul.main-nav a::text").getall()                  Kategoriler
# response.css("ul.main-nav a::attr(href)").getall()            Linkler

class QuotesSpider(scrapy.Spider):
    name = "quotes" 
    kategoriler = []
    linkler = []
    urun_liste=dict()
    url = "https://www.trendyol.com"
    start_urls = [
        'https://www.trendyol.com/telefon?siralama=4', 
    ] 
    top = 0
    urun_detay=[]

    def parse(self, response):
        self.urls =response.css("div.p-card-chldrn-cntnr a::attr(href)").getall()  

        next_url = self.url + self.urls[self.top] 
        self.top+=1
        yield scrapy.Request(url=next_url,callback=self.urunler) 
        

    def urunler(self,response): 
        marka = response.css("h1.pr-new-br::text").get()
        isim = response.css("h1.pr-new-br span::text").get()
        fiyat = response.css("span.prc-slg::text").get()
 
        lenOfPage=response.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match=False
        while(match==False):
            lastCount = lenOfPage 
            dgr_sayisi= response.css("div.pr-rnr-sm-p-s span::text").get()
            dgr_puan=response.css("div.pr-rnr-sm-p span::text").get()
            lenOfPage = response.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount == lenOfPage:
                match=True
 
        self.urun_detay.append((marka,isim,fiyat,dgr_sayisi,dgr_puan)) 
        with open("kategori.txt","w",encoding="UTF-8")as file: 
            file.write(marka+"\n") 
            file.write(isim+"\n") 
            file.write(fiyat+"\n") 
            file.write(dgr_sayisi+"\n")          
            file.write(dgr_puan+"\n")          