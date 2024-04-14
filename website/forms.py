from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your email address'}))
    first_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your first name'}))
    last_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your last name'}))