from django import forms
from .models.post import Post
from .models.base import User
from .models.user import Profile
from django.contrib.auth.forms import UserCreationForm

class AddPost(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ['title', 'body']

class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class EditProfile(forms.Form):
    username = forms.CharField(max_length=140)
    email = forms.EmailField()
    bio = forms.CharField(max_length=1000)

class Login(UserCreationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password'}))

class Search(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'class': 'search', 'placeholder': 'Type something'}))