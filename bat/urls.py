from django.urls import path , include 
from django.contrib import admin
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
     
    path('', views.batpage , name='bat'),
     
]
