import scrapy


class QuotesSpider(scrapy.Spider):
    name = "books"
    page_count=0
    book_count=1
    start_urls=[
        "https://www.kitapyurdu.com/index.php?route=product/best_sellers&list_id=1&filter_in_stock=1&filter_in_stock=1&page=1"
    ]

    file = open("books.txt","a",encoding="UTF-8")

    def parse(self, response):
        book_names = response.css("div.name.ellipsis a span::text").extract()
        book_authors = response.css("div.author span a span::text").extract()
        book_publishers = response.css("div.publisher span a span::text").extract()
        i=0
        while(i<len(book_names)):
            
            """                              json dosyasına yazdırma
            yield{
                "name":book_names[i],
                "author":book_authors[i],
                "publisher":book_publishers[i]
            }
            """

            self.file.write("********************************\n")
            self.file.write(str(self.book_count)+".\n")
            self.file.write("Kitap ismi : " +book_names[i] +"\n")
            self.file.write("Yazar : " +book_authors[i] +"\n")
            self.file.write("Yayınevi : " +book_publishers[i] +"\n")
            self.file.write("**********************************\n")
            
            i +=1
            self.book_count +=1

        next_url =response.css("a.next::attr(href)").extract_first()
        self.page_count +=1
        if next_url is not None and self.page_count !=5:
            yield scrapy.Request(url=next_url,callback=self.parse)
        else:
            self.file.close()