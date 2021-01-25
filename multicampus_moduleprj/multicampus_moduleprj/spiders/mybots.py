import scrapy
from multicampus_moduleprj.items import MulticampusModuleprjItem
from scrapy.http import Request



URL= 'https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105#&date=%20210125&page=%s'
start_page = 1
print(URL % start_page)
print(URL.format(start_page))


class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    allowed_domains = ['naver.com']
    start_urls = [URL%start_page]
  
    def start_requests(self):
        for i in range(10):
            yield Request(url=URL %(i+start_page), callback=self.parse)

    def parse (self,response):
        titles = response.xpath('//*[@id="section_body"]/ul[1]/li/dl/dt[2]/a').extract()
        writers = response.css('.writing::text').extract()
        previews = response.css('.lede::text').extract()

        
        items = []
       
        for idx in range(len(titles)):
            item = MulticampusModuleprjItem()
            item['title'] = titles[idx]
            item['writer'] = writers[idx]
            item['preview'] = previews[idx]

            items.append(item)

        return items
