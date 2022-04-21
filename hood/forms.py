from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import EmailInput, TextInput, PasswordInput, FileInput, Select

from .models import Business, Neighborhood, Post, Services


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


class CreateJoinHoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = ['neighborhoodName', 'location']
        widgets = {
            'neighborhoodName': TextInput(attrs={'class': 'form-control'}),
            'location': TextInput(attrs={'class': 'form-control'})
        }


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'postBody']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'postBody': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'})
        }


class CreateService(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['serviceName', 'servicePhone',
                  'serviceEmail', 'serviceDescription']
        widgets = {
            'serviceName': TextInput(attrs={'class': 'form-control'}),
            'serviceDescription': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'servicePhone': TextInput(attrs={'class': 'form-control'}),
            'serviceEmail': TextInput(attrs={'class': 'form-control'}),
        }


class CreateBusiness(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['businessName', 'businessPhone',
                  'businessEmail', 'bussinessDescription']
        widgets = {
            'businessName': TextInput(attrs={'class': 'form-control'}),
            'businessPhone': TextInput(attrs={'class': 'form-control'}),
            'businessEmail': TextInput(attrs={'class': 'form-control'}),
            'bussinessDescription': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }
