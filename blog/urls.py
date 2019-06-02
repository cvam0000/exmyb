from django.contrib import admin
from django.urls import path , include
from . import views 



urlpatterns = [
    path('', views.post_list, name='blog'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    
]