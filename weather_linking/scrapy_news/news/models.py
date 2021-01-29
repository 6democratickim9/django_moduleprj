
from django.db import models

# # class sports_news(models.Model):
# #     title = models.CharField(max_length=100)
# #     time =  models.CharField(max_length=100)
# #     preview = models.CharField(max_length=100)

class it_news(models.Model):
    title = models.CharField(max_length=100,unique=True)
    time = models.CharField(max_length=100,unique=True)
    preview = models.CharField(max_length=500,unique=True)
    
    def __str__(self):


        return self.title
    


# class ec_news(models.Model):
#     title = models.CharField(max_length=100)
#     time = models.CharField(max_length=100)
#     preview = models.CharField(max_length=100)

#     def __str__(self):
#         return self.title
# # Create your models here.
