
import scrapy
from scrapy_djangoitem import DjangoItem

import sys
sys.path.append('C:/Users/MIN/Desktop/module_project/weather_linking/scrapy_news/news')

from news.models import it_news


class ScrapyItnews(DjangoItem):
    django_model = it_news
    title = scrapy.Field()
    time = scrapy.Field()
    preview = scrapy.Field()

