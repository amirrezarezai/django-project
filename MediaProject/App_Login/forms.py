from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from App_Login.models import UserProfile

class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Your Email'}))
    username = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Your Username'}))
    password1 = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}))
    password2 = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder': 'confirm password'}))
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'username'}))
    password = forms.CharField(required=True, label='', widget=forms.PasswordInput(attrs={'placeholder': 'password'}))


class EditUserProfile(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'type':'date',}))
    class Meta:
        model=UserProfile
        exclude=('user',)
