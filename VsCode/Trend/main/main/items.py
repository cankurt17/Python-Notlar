# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class trendyolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field() 
    marka = scrapy.Field()
    isim = scrapy.Field()
    fiyat = scrapy.Field()
    degerlendirme = scrapy.Field()
    puan = scrapy.Field()
    yorum = scrapy.Field()

    pass
    
