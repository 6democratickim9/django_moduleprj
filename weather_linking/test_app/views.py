from django.shortcuts import render
from .models import it_news


def save_it_news(request):
    # it_news_view = {
    #     "title" = ["title"],
    #     "time" = ["time"], 
    #     "preview" = ["preview"],
    # }

    it_news(
        title = ["title"],
        time = ["time"], 
        preview = ["preview"]
    ).save()

    return render(request, 'news_app/save_success.html')