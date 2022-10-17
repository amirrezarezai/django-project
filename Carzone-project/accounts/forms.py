from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class Signup(UserCreationForm):
    email = forms.EmailField(label='',required=True,widget=forms.EmailInput(attrs={'placeholder':'emai','class':'input-text'}))
    first_name = forms.CharField(label='',max_length=250,widget=forms.TextInput(attrs={'placeholder':'first name','class':'input-text'}),required=True)
    last_name = forms.CharField(label='',max_length=250,widget=forms.TextInput(attrs={'placeholder': 'last name', 'class': 'input-text'}),required=True)
    username = forms.CharField(label='',max_length=250,required=True,widget=forms.TextInput(attrs={'placeholder': 'username', 'class': 'input-text'}))
    password1 = forms.CharField(label='',max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'password','class':'input-text'}),required=True)
    password2 = forms.CharField(label='',max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'confirm password','class':'input-text'}),required=True)
    class Meta:
        model = User
        fields =['first_name','last_name','username','email','password1','password2']


class Login_form(AuthenticationForm):
    username = forms.CharField(label='',max_length=250,required=True,widget=forms.TextInput(attrs={'placeholder': 'username', 'class': 'input-text'}))
    password = forms.CharField(label='',max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'password','class':'input-text'}),required=True)
    class Meta:
        model =User
        fields = ['username','password']

