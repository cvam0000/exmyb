
from django.shortcuts import render
from .forms import AnsForm 
from .models import Bat
from django.shortcuts import render, redirect
from django.utils import timezone

# Create your views here.
from django.shortcuts import render_to_response
def batpage(request):
    #if request.user.is_authenticated:
    posts = Bat.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'bat/bat.html', {'posts': posts})
       
   # else :
      #return render('home')   
      