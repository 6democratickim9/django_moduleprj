from django.contrib import admin
from .models import today_weather_db, weather_data_db

admin.site.register(today_weather_db)
admin.site.register(weather_data_db)
