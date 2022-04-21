from dataclasses import fields
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import EmailInput, TextInput, PasswordInput, FileInput, Select

from .models import Neighborhood, Post


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'username': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class LoginUserForm(forms.Form):

    username = forms.CharField(widget=TextInput(
        attrs={'class': 'form-control'}), max_length=100)
    password = forms.CharField(widget=PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['class'] = 'form-control'


class createJoinHoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = ['neighborhoodName', 'location']
        widgets = {
            'neighborhoodName': TextInput(attrs={'class': 'form-control'}),
            'location': TextInput(attrs={'class': 'form-control'})
        }


class createPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'postBody']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'postBody': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'})
        }