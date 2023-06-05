from django.contrib.auth.models import User
from django.contrib.contenttypes import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'sing_name', 'placeholder': "Name"}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'sing_name', 'placeholder': "Email or Phone Number"}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'sing_name', 'placeholder': "Password"}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'sing_name', 'placeholder': "Password Confirmation"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'sing_name', 'placeholder': "Name"}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'sing_name', 'placeholder': "Password"}))
