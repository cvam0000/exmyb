

from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    data = Post.objects.all()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    dataBlog = {"blog": data }
    
    return render(request, 'blog/blog.html', dataBlog )