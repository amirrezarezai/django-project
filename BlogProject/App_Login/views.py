from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login , logout ,authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_Login.forms import Signup,User_Change_profile,ProfilePic
from .models import userProfile
# Create your views here.
def sign_up(request):
    form = Signup()
    register = False
    if request.method == 'POST':
        form = Signup(data=request.POST)
        if form.is_valid():
            form.save()
            register=True

    context = {'form':form , 'register':register}
    return render(request,'App_Login/sign_up.html',context=context)

def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
    context = {'form':form}
    return render(request,'App_Login/login.html',context=context)

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('signin'))

@login_required
def profileViews(request):
    user = userProfile.objects.all()
    context={}
    return render(request,'App_Login/profile.html',context=context)

@login_required
def changeView(request):
    current_user = request.user
    form = User_Change_profile(instance=current_user)
    if request.method == 'POST':
        form = User_Change_profile(request.POST,instance=current_user)
        if form.is_valid():
            form.save()
            form = User_Change_profile(instance=current_user)
            return HttpResponseRedirect(reverse('profile'))
    return render(request,'App_Login/profile_change.html',{'form':form})

@login_required
def passwordChangeView(request):
    current_user = request.user
    change = False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user,data=request.POST)
        if form.is_valid():
            form.save()
            change=True
    return render(request,'App_Login/password_change.html',context={'form':form , 'change':change})

@login_required
def add_profile_pic(requset):
    form = ProfilePic()
    if requset.method == 'POST':
        form = ProfilePic(requset.POST,requset.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = requset.user
            user_obj.save()
            return HttpResponseRedirect(reverse('profile'))
    return render(requset, 'App_Login/changePic.html',context={'form':form})

@login_required
def change_pro_pic(request):
    form = ProfilePic(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProfilePic(request.POST,request.FILES,instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    return render(request,'App_Login/changePic.html',context={'form':form})