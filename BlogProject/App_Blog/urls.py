from django.urls import path
from . import views

app_name = 'App_Blog'

urlpatterns = [
    path('',views.BlogList.as_view(),name='blog_list'),
    path('write/',views.CreateBlog.as_view(),name='create_blog'),
    path('details/(?P<slug>[-a-zA-Z0-9_]+)\\Z',views.blog_details,name='blog_details'),
    path('liked/<pk>',views.like,name='liked'),
    path('unliked/<pk>',views.unliked,name='unliked'),
    path('myblog/',views.myBlog.as_view(),name='myblog'),
    path('editblog/<pk>',views.updateBlog.as_view(),name='editBlog')
]