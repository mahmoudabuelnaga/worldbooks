from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import CustomUser

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,required=False)
    last_name = forms.CharField(max_length=100,required=False)
    email = forms.EmailField(help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
