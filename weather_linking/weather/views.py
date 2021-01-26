from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/onecall?lat=37.566535&lon=126.977969&exclude=minutely,hourly,alerts&appid=43fcd06479e874bea4eb2b675ab6b465'
    
    
    if request.method == "POST":
        pass

    r = requests.get(url).json()
    current = r["current"]
    daily_list = r["daily"]

    today_weather = {
        "temp": round((current["temp"] - 271.94), 2),
        "main": current["weather"][0]["main"],
        "description" : current["weather"][0]["description"],
        "icon": current["weather"][0]["icon"]
    }

    weather_data = []
    for index, daily in enumerate(daily_list):
        daily_weather = {
            "day": index,
            "main": daily["weather"][0]["main"],
            "description" : daily["weather"][0]["description"],
            "icon": daily["weather"][0]["icon"]
        }
        weather_data.append(daily_weather)
    del weather_data[0]
    context = {
        'weather_data' : weather_data, 
        'today_weather' : today_weather    
    }

    return render(request, 'weather/weather.html', context)
