from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
def inedex(request):
    return HttpResponseRedirect(reverse('App_Blog:blog_list'))