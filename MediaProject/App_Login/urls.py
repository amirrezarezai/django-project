from django.urls import path
from . import views

app_name = 'App_Login'

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login_page,name='login'),
    path('editprofile/',views.edit_Profile,name='editProfile'),
    path('logout/',views.logout_user,name='logout'),
    path('Profile/',views.Profile,name='Profile'),
    path('user/<username>/',views.user, name='user'),
    path('follow/<username>/',views.follow, name='follow'),
    path('unfollow/<username>/',views.unfollow, name='unfollow'),
]