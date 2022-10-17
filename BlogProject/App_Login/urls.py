from django.urls import path
from . import views
urlpatterns = [
    path('signup/',views.sign_up,name='signup'),
    path('signin/',views.login_page,name='signin'),
    path('logout/',views.logout_user,name='logout'),
    path('profile/',views.profileViews,name='profile'),
    path('Change_profile/',views.changeView,name='changeProfile'),
    path('Change_password/',views.passwordChangeView,name='changePassword'),
    path('Change_picture/',views.add_profile_pic,name='changePicture'),
    path('update_picture/',views.change_pro_pic,name='updatePicture'),
]