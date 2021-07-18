import scrapy
import requests
from scrapy.http.response.text import TextResponse

url_short = 'https://assets.datacamp.com/production/repositories/2560/datasets/19a0a26daa8d9db1d920b5d5607c19d6d8094b3b/all_short'

class DCSpider(scrapy.Spider): 
    name = "data-camp-spider"
    def start_requests(self): 
        yield scrapy.Request(url = url_short, callback = self.parse)

    def parse(self, response): 
        author_names = response.css('p.course-block__author-name::text').extract()
        return author_names

class DCdescr( scrapy.Spider ):
    name = 'dcdescr'
    
    def start_requests( self ):
        yield scrapy.Request( url = url_short, callback = self.parse )

    def parse( self, response ):
        links = response.css( 'div.course-block > a::attr(href)' ).extract()
        for link in links:
            yield response.follow(url=link, callback=self.parse_descr)

    
    def parse_descr( self, response ):
        course_descr = response.css( 'p.course__description::text' ).extract_first()
        yield course_descr


def inspect_class(c):
    newc = c()
    meths = dir(newc)
    if 'name' in meths:
        print("Your spider class name is:", newc.name)
    if 'from_crawler' in meths: 
        print("It seems you have inherited methods from scrapy.Spider -- NICE!")
    else:
        print("Oh no! It doesn\'t seem that you are inheriting the methods from scrapy.Spider!!")

def inspect_spider( s ):
    news = s()  
    try:
        req1 = list( news.start_requests() )[0]
        html1 = requests.get( req1.url ).content
        response1 = TextResponse( url = req1.url, body = html1, encoding = 'utf-8' )
        req2 = list( news.parse( response1 ) )[0]
        html2 = requests.get( req2.url ).content
        response2 = TextResponse( url = req2.url, body = html2, encoding = 'utf-8' )
        for d in news.parse_descr( response2 ):
            print("One course description you found is:", d )
            break
    except:
        print("Oh no! Something is wrong with the code. Keep trying!")



#inspect_spider(DCSpider)
#inspect_spider(DCdescr)
