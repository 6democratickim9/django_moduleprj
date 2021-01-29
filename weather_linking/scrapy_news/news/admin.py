

from django.contrib import admin
from .models import it_news



class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'time',
        'preview'
    )
admin.site.register(it_news)
# Register your models here.
