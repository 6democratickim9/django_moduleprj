from django.contrib import admin
from .models import it_news

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','preview','time')
    search_fields = ('title','content')
    
admin.site.register(it_news)
# Register your models here.
