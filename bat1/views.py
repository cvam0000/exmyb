from django.shortcuts import render
from .models import Answers_Bat1 ,Bat1_ques
from .forms import Ans_bat1
from django.http import HttpResponse





def bat1(request):

    if request.method == 'POST':
        form = Ans_bat1(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(content="some content")
            #return render(request, 'bat/bat.html',context_instance=RequestContext(request))
            #return render(request, 'bat/bat.html',{})            
            
            
    else:
        
        data = Bat1_ques.objects.all()
        form = Ans_bat1()
        m = zip(data,form)
        quesans = {"ques": data , "form": form  }
        return render(request, 'bat/bat1.html', {'m':m})










