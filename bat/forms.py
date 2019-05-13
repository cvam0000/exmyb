from django.forms import ModelForm
from .models import Bat

class AnsForm(ModelForm):
    class Meta:
         model = Bat
         fields = ['answer']