from django.urls import path
from . import views
urlpatterns = [
path('',views.foodView, name='food'),
path('delete/<int:id>/',views.remove,name='delete')
]