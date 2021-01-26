# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MulticampusModuleprjItem_it(scrapy.Item):
    title_it = scrapy.Field()
    writer_it = scrapy.Field()
    preview_it = scrapy.Field()

class MulticampusModuleprjItem_ec(scrapy.Item):
    title_ec = scrapy.Field()
    writer_ec = scrapy.Field()
    preview_ec = scrapy.Field()