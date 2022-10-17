from django.shortcuts import render,HttpResponseRedirect
from App_Login.forms import CreateNewUser,LoginUserForm,EditUserProfile
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse,reverse_lazy
from App_Login.models import UserProfile,Follow
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from App_Posts.forms import PostForm
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('App_Login:login'))

    return render(request,'App_Login/Signup.html',context={'form':form,'registered':registered})

def login_page(request):
    form = LoginUserForm()
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('App_Posts:home'))

    return render(request,'App_Login/login.html',context={'form':form})

@login_required
def edit_Profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = EditUserProfile(instance=current_user)

    if request.method == 'POST':
        form = EditUserProfile(request.POST,request.FILES,instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = EditUserProfile(instance=current_user)
            return HttpResponseRedirect(reverse('App_Login:Profile'))

    return render(request, 'App_Login/editProfile.html',context={'form':form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:login'))

@login_required
def Profile(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('App_Posts:home'))


    return render(request,'App_Login/user.html',context={'form':form})
@login_required
def user(request,username):
    user_other = User.objects.get(username=username)
    already_followed = Follow.objects.filter(follower=request.user, following=user_other)
    if user == request.user:
        return HttpResponseRedirect(reverse('App_Login:Profile'))

    return render(request,'App_Login/user_other.html',context={'user_other':user_other,'already_followed':already_followed})

@login_required
def follow(request,username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user,following=following_user)
    if not already_followed:
        followed_user = Follow(follower=follower_user,following=following_user)
        followed_user.save()
    return HttpResponseRedirect(reverse('App_Login:user', kwargs={'username':username}))

@login_required
def unfollow(request,username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.get(follower=follower_user,following=following_user)
    already_followed.delete()
    return HttpResponseRedirect(reverse('App_Login:user', kwargs={'username':username}))









