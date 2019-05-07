from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
def adminPage(request):
   if request.user.is_superuser:
      return render_to_response('admin_exmyb/admin.html')
   else :
      return render('home')   