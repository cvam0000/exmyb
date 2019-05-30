from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,  help_text='Required. .')
    last_name = forms.CharField(max_length=30,  help_text='Required. .')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phone = forms.CharField(max_length=12 , help_text='Required. Inform a valid Phone no.')
    account_type = forms.TypedChoiceField(coerce=lambda x: x =='True', choices=((False, 'starup'), (True, 'investor')))
                               
    class Meta:
        model = User
        fields = ('username','email', 'first_name', 'last_name', 'phone', 'password1', 'password2', )



class OtpForm(forms.Form):
    otp =forms.CharField(max_length=30,help_text='should enter an otp')
    class Meta:
        fields=('otp')



class EditProfileForm(forms.ModelForm):

    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email=forms.CharField(label='email')
    phone= forms.CharField(label='phone')   
    

    class Meta:
        model = User
        fields = ['first_name', 'last_name' , 'email', 'phone']