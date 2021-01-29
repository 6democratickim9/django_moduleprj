# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
# from .items import ScrapyItnews

import sys
sys.path.append('C:/Users/MIN/Desktop/module_project/weather_linking/scrapy_news/news')

from news.models import it_news


class ScrapyNewsPipeline_it(object):

    def process_item(self, item, spider):
        title = item['title']
        time = item['time']
        preview = item['preview']

        it_news.objects.create(
            title = title,
            time = time,
            preview = preview
        )

        
        return item


# class ScrapyNewsPipeline_ec:
#     def process_item(self, item, spider):
#         title_ec = item['title_ec']
#         time_ec = item['time_ec']
#         preview_ec = item['preview_ec']

#         it_news.objects.create(
#             title_ec = title_ec,
#             time_ec = time_ec,
#             preview_ec = preview_ec
#         )

        
#         return item

