from multicampus_moduleprj.items import MulticampusModuleprjItem_ec, MulticampusModuleprjItem_it
import scrapy
from scrapy.http import Request

# def remove_space(titles:list) -> list:
#     result = []
#     # 공백 제거
#     for i in range(len(titles)):
#         if len(titles[i].strip()) >0:
#             result.append(titles[i].strip())
 
#     return result




URL_IT = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=105/&page=%s'
start_page = 1
URL_EC='https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=101&sid2=101/&page=%s'

class MybotsSpider(scrapy.Spider):
    name = 'ec_mybots'
    allowed_domains = ['naver.com']
    start_urls = [URL_EC%start_page]
    # print("------------------->", start_urls)
    def start_requests(self):
        # print("chk1----------------------------------")
        for i in range(5):
            yield Request(url=URL_EC%(i+start_page), callback=self.parse, dont_filter=True)

    def parse (self,response):
        # test = response.xpath('').extract()
        previews_ec = response.css('.lede::text').extract()
        writers_ec = response.css('.writing::text').extract()
        titles_upperec = response.xpath('//*[@id="main_content"]/div[2]/ul[2]/li/dl/dt[2]/a/text()').extract()
        titles_npic_it = response.xpath('//*[@id="main_content"]/div[2]/ul[2]/li/dl/dt/a/text()').extract()

        # print("-------------->", test)
        # print("-------------->", writers)
        # print("-------------->", previews)
        
        items = []
        
       
        for idx in range(len(titles)):
            item = MulticampusModuleprjItem_ec()
            item['preview'] = previews[idx]
            item['writer'] = writers[idx]
            item['title'] = titles[idx]
            

            items.append(item)
        # print("--------------2>", items)
        return items

class MybotsSpider(scrapy.Spider):
    name = 'it_mybots'
    allowed_domains = ['naver.com']
    start_urls = [URL_IT%start_page]
    # print("------------------->", start_urls)
    def start_requests(self):
        # print("chk1----------------------------------")
        for i in range(5):
            yield Request(url=URL_IT%(i+start_page), callback=self.parse, dont_filter=True)

    def parse (self,response):
        # test = response.xpath('').extract()
        previews_it = response.css('.lede::text').extract()
        writers_it = response.css('.writing::text').extract()
        titles_pic_it = response.xpath('//*[@id="main_content"]/div[2]/ul[2]/li/dl/dt[2]/a/text()').extract() 
        titles_npic_it = response.xpath('//*[@id="main_content"]/div[2]/ul[2]/li/dl/dt/a/text()').extract()

        # print("-------------->", test)
        # print("-------------->", writers)
        # print("-------------->", previews)
        
        items = []
        
       
        for idx in range(len(titles_pic_it)):
            item = MulticampusModuleprjItem_it()
            item['preview'] = previews_it[idx]
            item['writer'] = writers_it[idx]
            item['title'] = titles_pic_it[idx]
            item['title'] = titles_npic_it[idx]

            

            items.append(item)
        # print("--------------2>", items)
        return items
