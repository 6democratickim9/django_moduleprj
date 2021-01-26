import scrapy
from multicampus_moduleprj.items import MulticampusModuleprjItem
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



class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    allowed_domains = ['naver.com']
    start_urls = [URL_IT%start_page]
    # print("------------------->", start_urls)
    def start_requests(self):
        # print("chk1----------------------------------")
        for i in range(10):
            yield Request(url=URL_IT%(i+start_page), callback=self.parse, dont_filter=True)

    def parse (self,response):
        # test = response.xpath('').extract()
        previews = response.css('.lede::text').extract()
        writers = response.css('.writing::text').extract()
        titles = response.xpath('//*[@id="main_content"]/div[2]/ul[2]/li/dl/dt[2]/a/text()').extract()
        # print("-------------->", test)
        # print("-------------->", writers)
        # print("-------------->", previews)
        
        items = []
        
       
        for idx in range(len(titles)):
            item = MulticampusModuleprjItem()
            item['preview'] = previews[idx]
            item['writer'] = writers[idx]
            item['title'] = titles[idx]
            

            items.append(item)
        # print("--------------2>", items)
        return items
