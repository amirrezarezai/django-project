from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from .models import Link_model
# Create your views here.

def scrap(request):
    if request.method == 'POST':
        site = request.POST.get('site','')
        page = requests.get(site)
        soup = BeautifulSoup(page.text,'html.parser')


        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Link_model.objects.create(address=link_address,name=link_text)
        return HttpResponseRedirect('/')
    else:
        data = Link_model.objects.all()

    return render(request,'base.html',{'data':data})

def clear(request):
    data = Link_model.objects.all().delete()
    return render(request,'base.html')