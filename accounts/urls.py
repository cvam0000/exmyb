from django.urls import path , include 
from django.contrib import admin
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
     path('admin/', admin.site.urls),
     path('user/', include('django.contrib.auth.urls')),
     path('user/signup/' , views.signup, name='signup'),
     path('user/signup/phone-verification' , views.validate, name='otp'),
     path('', TemplateView.as_view(template_name='home.html'), name='home'),
     path('auth/',include('social_django.urls',namespace='social' )),
]
