from django.urls import path
from . import views
urlpatterns = [
    path('',views.CVform , name='CVform'),
    path('<int:id>/',views.resume , name='resume'),
    path('list/',views.list, name ='list')
]
