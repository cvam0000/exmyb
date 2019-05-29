
from django.shortcuts import render

from .models import Bat_textquestions,Mcq
from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import render_to_response

def batpage(request):
    #if request.user.is_authenticated:
    posts = Bat.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'bat/bat1.html', {'posts': posts})
       
   # else :
      #return render('home')   
      