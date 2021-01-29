from django.contrib import admin
from .models import it_news

class it_newsAdmin(admin.ModelAdmin):
    pass
admin.site.register(it_news,it_newsAdmin)

# Register your models here.
