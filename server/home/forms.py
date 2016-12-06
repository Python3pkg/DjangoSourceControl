from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from django.conf import settings


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=32, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=32, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
