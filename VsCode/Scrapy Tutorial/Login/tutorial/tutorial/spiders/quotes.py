import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://quotes.toscrape.com/login', 
    ]

    def parse(self, response): 
        token = response.css("form input::attr(value)").extract_first()
        return FormRequest.from_response(response,formdata={
            'crsf_token':token,
            'username':"admin",
            'password':"1"
        },callback=self.start)
        
    def start(self,response):
        open_in_browser(response)
        print("Burdayım")
