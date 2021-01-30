
from django.db import models


class it_news(models.Model):
    title = models.CharField(max_length=100,unique=True)
    time = models.CharField(max_length=100)
    preview = models.CharField(max_length=500,unique=True)