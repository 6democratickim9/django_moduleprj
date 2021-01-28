# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy_news.items import scrapy_itnews
from news.models import it_news

class ScrapyNewsPipeline_it:
    def process_item(self, item, spider):
        title = item['title']
        time = item['time']
        preview = item['preview']

        scrapy_itnews.objects.create(
            title = title,
            time = time,
            preview = preview
        )

        
        return item

