from . import views
from django.urls import path

urlpatterns = [
    path('',views.scrap, name ='scrap'),
    path('delete/',views.clear)
]