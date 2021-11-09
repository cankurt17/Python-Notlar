import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.instagram.com/accounts/login/' 
    ]

    def parse(self, response): 
        print("cankurt")
        token = response.css("form input::attr(value)").extract_first() 
        return FormRequest.from_response(response,formdata={ 
            'username':"cankurt46",
            'password':"29963207974"
        },callback=self.start)
        
    def start(self,response):
        open_in_browser(response)
        print("Burdayım")
