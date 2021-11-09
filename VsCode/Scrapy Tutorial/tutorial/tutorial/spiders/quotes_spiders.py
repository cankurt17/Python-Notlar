import scrapy 
class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/'
    ]
 
    def parse(self, response):   
        with open("quotes.txt","w",encoding="UTF-8") as file:
            for quote in response.css("div.quote"): 
                title = quote.css("span.text::text").extract_first()
                author = quote.css("small.author::text").extract_first()
                tags = quote.css("div.tags a.tag::text").extract()
                file.write("*****************************\n")
                file.write("Alıntı :"+title+"\n")
                file.write("Alıntı sahibi :"+author+"\n")
                file.write("Etiketler :"+str(tags)+"\n")
        
