from scrapy_news import items
from django.db import models

# # class sports_news(models.Model):
# #     title = models.CharField(max_length=100)
# #     time =  models.CharField(max_length=100)
# #     preview = models.CharField(max_length=100)

class it_news(models.Model):
    title = models.CharField(max_length=100,unique=True)
    time = models.CharField(max_length=100)
    preview = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
# # class ec_news(models.Model):
# #     title = models.CharField(max_length=100)
# #     time = models.CharField(max_length=100)
# #     preview = models.CharField(max_length=100)
    
# # Create your models here.
