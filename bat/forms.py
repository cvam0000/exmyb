from django.forms import ModelForm
from .models import Ans

class AnsForm(ModelForm):
    class Meta:
         model = Ans
         fields = ['answer']