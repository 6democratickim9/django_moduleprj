from scrapy_news.items import scrapy_itnews
import scrapy
from scrapy.http import Request

def remove_space(titles_npic:list) -> list:
    result = []
    # 공백 제거
    for i in range(len(titles_npic)):
        if len(titles_npic[i].strip()) >0:
            result.append(titles_npic[i].strip())
 
    return result




URL_IT = 'https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=105&page=%s'

start_page = 1

class MybotsSpider(scrapy.Spider):
    name = 'mybots_it'
    allowed_domains = ['naver.com']
    start_urls = [URL_IT%start_page]
    # print("------------------->", start_urls)
    def start_requests(self):
        # print("chk1----------------------------------")
        for i in range(10):
            yield Request(url=URL_IT%(i+start_page), callback=self.parse)

    def parse (self,response):
        # test = response.xpath('').extract()
        previews = response.css('.lede::text').extract()
        times = response.xpath('//*[@id="main_content"]/div[2]/ul[1]/li/dl/dd/span[3]/text()').extract()
        titles_npic= response.xpath('//*[@id="main_content"]/div[2]/ul[1]/li/dl/dt/a/text()').extract()
        converted_space= remove_space(titles_npic)
        
        
        items = []
        
       
        for row in zip(converted_space,times,previews):
            item = scrapy_itnews()
            item['title'] = row[0]
            item['time'] = row[1]
            item['preview'] = row[2]
        

            yield item #제너레이터