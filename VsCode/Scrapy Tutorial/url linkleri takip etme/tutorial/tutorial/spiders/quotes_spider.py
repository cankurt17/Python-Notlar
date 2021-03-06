
import scrapy 

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    quote_count=1
    start_urls = [
        'http://quotes.toscrape.com/page/1/', 
    ]
    file = open("quotes.txt","a",encoding="UTF-8")
 
    def parse(self, response):    
        for quote in response.css("div.quote"): 
            title = quote.css("span.text::text").extract_first()
            author = quote.css("small.author::text").extract_first()
            tags = quote.css("div.tags a.tag::text").extract()
            self.file.write(str(self.quote_count)+"*****************************\n")
            self.file.write("Alıntı :"+title+"\n")
            self.file.write("Alıntı sahibi :"+author+"\n")
            self.file.write("Etiketler :"+str(tags)+"\n")
            self.quote_count +=1      
               
        next_url = response.css("li.next a::attr(href)").extract_first() 
        
        if next_url is not None:
            next_url = "http://quotes.toscrape.com"+next_url
            yield scrapy.Request(url=next_url, callback=self.parse)
        else:
            self.file.close()
        
    