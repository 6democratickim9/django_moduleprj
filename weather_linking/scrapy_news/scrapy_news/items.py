# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from news.models import sports_news, it_news, ec_news



class MulticampusModuleprjItem_it(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    preview = scrapy.Field()


class MulticampusModuleprjItem_ec(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    preview = scrapy.Field()



class MulticampusModuleprjItem_sp(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    preview = scrapy.Field()

class ec_newsItem(DjangoItem):
    django_model = ec_news
    
    
class sports_newsItem(DjangoItem):
    title = sports_news["title"]
    time = sports_news["time"]
    preview = sports_news["preview"]


class MulticampusModuleprjItem_itItem(DjangoItem):
    django_model = it_news