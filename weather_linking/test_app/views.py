from django.shortcuts import render
from .models import it_news
from django.views.generic.edit import FormView
from .forms import PostSearchForm
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import RefreshForm
import os

class NewsLV(ListView):
    model = it_news
    template_name = "news/news_all.html"
    context_object_name = "news" 

    paginate_by = 10

class RefreshFormView(FormView):
    template_name = "news/news_all.html"
    form_class = RefreshForm
    success_url = '/news/list'
    context_object_name = "news" 

    paginate_by = 10


    def form_valid(self, form):
        print(self.request)
        os.chdir('C:\Users\MIN\Desktop\module_project\weather_linking\news_app\news_app')
        os.system('scrapy crawl mybots_it')
        return super().form_valid(form)

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = "blog/post_search.html"

    def form_valid(self,form):
        schword= self.request.POST['search_word']

        post_list= Post.objects.filter( Q(title__icontains = schword)| Q(description__icontains= schword)|Q(content__icontains=schword)).distinct()

        #검색된 결과
        context={}

        context['form'] = form
        context['search_keyword']=schword
        context['search_list']=post_list
        print(post_list)

        return render(self.request, self.template_name,context)