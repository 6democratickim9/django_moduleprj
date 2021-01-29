from django.shortcuts import render
from scrapy_news.news.models import it_news


def save_it_news(request):
    it_news_view = {
        "title" = ["title"],
        "time" = ["time"], 
        "preview" = ["preview"],
    }

    it_news(
        title = ["title"],
        time = ["time"], 
        preview = ["preview"]
    ).save()

    return render(request, 'scrapy_news/save_success.html')

# Create your views here.
