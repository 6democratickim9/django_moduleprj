from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  #the path for our index view
    path('save/', views.save_weather),
    path('view/', views.view_weather)
]
