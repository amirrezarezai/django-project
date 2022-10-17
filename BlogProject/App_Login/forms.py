from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from App_Login.models import userProfile

class Signup(UserCreationForm):
    emai = forms.EmailField(label='Email Address',required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class User_Change_profile(UserChangeForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password']

class ProfilePic(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = ['profile_pic']
