from django.urls import path , include 
from django.contrib import admin
from django.views.generic.base import TemplateView
from . import views



urlpatterns = [
    path('exmyb', views.about ,name="about"),
    path('policy' , views.policy, name="policy"),
    path( 't&c' ,views.tc, name="tc"),
    path( 'faq' ,views.faq, name="faq"),
    path( 'investors' ,views.investor, name="investor"),
    path( 'startups' ,views.startup, name="startup"),
    path('services',views.services, name="services")
   # path(  , nsme =""),
    
]
