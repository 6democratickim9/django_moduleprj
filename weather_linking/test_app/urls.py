from django.urls import path
from .views import *

app_name = 'it_news'

urlpatterns = [
    path('list', NewsLV.as_view(), name='list'),
    path('refresh', RefreshFormView.as_view(), name='refresh'),
    path('search/',SearchFormView.as_view(), name='search'),
]