from django import forms
from django.contrib.auth.models import User
from .models import CustomUser
# Create your models here.

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','password']


class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta :
        model = CustomUser
        fields = ['email','username','first_name','last_name','phone_number','password']
        