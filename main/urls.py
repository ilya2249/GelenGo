from django.contrib import admin
from django.urls import path
from main import urls
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wist', views.wist, name='wist'),
    path('chill', views.chill, name='chill')
]