from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'static_pages/about.html')  



def policy(request):
    return render(request, 'static_pages/policy.html') 


def tc(request):
    return render(request, 'static_pages/t&c.html')



def faq(request):
    return render(request, 'static_pages/faq.html')



def investor(request):
    return render(request, 'static_pages/investor.html')


def startup(request):
    return render(request, 'static_pages/startup.html') 



def services(request):
    return render(request, 'static_pages/services.html')          