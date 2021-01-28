from scrapy_news import items
from django.db import models

class sports_news(models.Model):
    title = models.CharField(max_length=100)
    time =  models.CharField(max_length=100)
    preview = models.CharField(max_length=100)

class it_news(models.Model):
    title = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    preview = models.CharField(max_length=100)

class ec_news(models.Model):
    title = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    preview = models.CharField(max_length=100)
    
# Create your models here.
