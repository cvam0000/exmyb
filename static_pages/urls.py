from django.urls import path , include 
from django.contrib import admin
from django.views.generic.base import TemplateView
from . import views



urlpatterns = [
    path('', views.about ,name="about"),
    path('/policy' , views.policy, name="policy"),
    path( '/t&c' ,views.tc, name="tc"),
   # path(  , nsme =""),
    
]
