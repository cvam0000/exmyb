
from django.contrib import admin
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from accounts.forms import SignUpForm , OtpForm
from twilio.rest import Client


from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import EditProfileForm
from django.http import HttpResponseRedirect




def validate(request, format=None):
    if request.method == 'POST':
        form=OtpForm(request.POST)
        otp=request.POST.get('otp')
        if opt=='1234':
            return redirect('home')    
        
    else:
        form = OtpForm()
        return render(request, 'otp.html', {'form': form})

def send_otp(no):
    account_sid = 'AC0dcc845ac9bc66a094fe66ed6701e9f0'
    auth_token = 'fc96afc0e5ea9a77a27de2658693fe5b'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            body= 'Your OTP For EXMYB.com Login is 1234 ' ,
            from_='+12063396691',
            status_callback='http://postb.in/1234abcd',
            to="+91"+no
        )

       
   




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


    


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })

        
       
         

            
def admin_login(request):
    return render(admin.site.urls)
    





def profile_view(request):
    user = request.user
    form = EditProfileForm(initial={'first_name':user.first_name, 'last_name':user.last_name})
    context = {
        "form": form
    }
    return render(request, 'home.html', context)

def edit_profile(request):

    user = request.user
    form = EditProfileForm(request.POST or None, initial={'first_name':user.first_name, 'last_name':user.last_name})
    if request.method == 'POST':
        if form.is_valid():


            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email=request.POST['email']
            user.phone=request.POST['phone']

            user.save()
            return HttpResponseRedirect('%s'%('profile'))

    context = {
        "form": form
    }

    return render(request, "editprofile.html", context)