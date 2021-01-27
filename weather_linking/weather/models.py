from django.db import models

class today_weather_db(models.Model):
    real = models.BooleanField(default=True)
    main = models.CharField(max_length=30)
    description = models.CharField(max_length=120)



    

    