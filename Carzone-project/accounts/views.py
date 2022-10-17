from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from .forms import Signup,Login_form
from django.contrib.auth import login , logout ,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
def login_user(request):
    form = Login_form()
    if request.method == 'POST':
        form =Login_form(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None :
                login(request,user)
                return HttpResponseRedirect(reverse('pages:home'))

    return render(request,'accounts/login.html',context={'form':form})


def register(request):
    form = Signup()
    register = False
    if request.method == 'POST':
        form = Signup(data=request.POST)
        if form.is_valid():
            form.save()
            register = True

    return render(request,'accounts/register.html',context={'form':form,'register':register,})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html', context={})
