import scrapy
from multicampus_moduleprj.items import MulticampusModuleprjItem
from scrapy.http import Request



URL = 'https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105#&date=20210125&page=%s'
start_page = 1



class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    allowed_domains = ['naver.com']
    start_urls = [URL%start_page]
    # print("------------------->", start_urls)
    def start_requests(self):
        # print("chk1----------------------------------")
        for i in range(10):
            yield Request(url=URL%(i+start_page), callback=self.parse)

    def parse (self,response):
        titles = response.xpath('//*[@id="section_body"]/ul[1]/li/dl/dt[2]/a/text()').extract()
        writers = response.css('.writing::text').extract()
        previews = response.css('.lede::text').extract()
        # print("-------------->", titles)
        # print("-------------->", writers)
        # print("-------------->", previews)
        
        items = []
        
       
        for idx in range(len(titles)):
            item = MulticampusModuleprjItem()
            item['title'] = titles[idx]
            item['writer'] = writers[idx]
            item['preview'] = previews[idx]

            items.append(item)
        # print("--------------2>", items)
        return items
