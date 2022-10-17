from django.shortcuts import render
from .models import Team
from cars.models import Car
# Create your views here.
def home(request):
    team = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    model_search = Car.objects.values_list('model',flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    body_search = Car.objects.values_list('body_style', flat=True).distinct()
    title_search = Car.objects.values_list('car_title', flat=True).distinct()
    all_cars = Car.objects.order_by('-created_date').all()
    return render(request,'pages/home.html',context={'team':team,'featured_cars':featured_cars,'all_cars':all_cars,
                                                     'model_search':model_search,
                                                     'city_search':city_search,
                                                     'body_search':body_search,
                                                     'title_search':title_search,})

def about(request):
    team = Team.objects.all()
    return render(request,'pages/about.html',context={'team':team})

def services(request):
    return render(request,'pages/services.html',context={})

def contact(request):
    return render(request,'pages/contact.html',context={})