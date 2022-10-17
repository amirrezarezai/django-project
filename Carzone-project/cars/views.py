from django.shortcuts import render,get_object_or_404
from .models import Car
from django.core.paginator import Paginator
# Create your views here.
def cars(request):
    all_car = Car.objects.order_by('-created_date').all()
    paginator = Paginator(all_car,4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    body_search = Car.objects.values_list('body_style', flat=True).distinct()
    title_search = Car.objects.values_list('car_title', flat=True).distinct()
    return render(request,'cars/cars.html',context={'all_car':paged_cars,
                                                    'model_search': model_search,
                                                    'city_search': city_search,
                                                    'body_search': body_search,
                                                    'title_search': title_search,
                                                    })

def car_detail(request,id):
    single_car = get_object_or_404(Car,pk=id)
    return render(request,'cars/car_detail.html',context={'single_car':single_car})

def search(request):
    cars = Car.objects.order_by('-created_date').all()
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    body_search = Car.objects.values_list('body_style', flat=True).distinct()
    title_search = Car.objects.values_list('car_title', flat=True).distinct()
    if 'keyword' in request.GET:
        keywords = request.GET['keyword']
        if keywords:
            cars = cars.filter(description__icontains=keywords)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    if 'body' in request.GET:
        body = request.GET['body']
        if body:
            cars = cars.filter(body_stayle__iexact=body)

    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            cars = cars.filter(car_title__iexact=title)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price,price__lte=max_price)


    return render(request,'cars/search.html',context={'cars':cars,
                                                      'model_search': model_search,
                                                      'city_search': city_search,
                                                      'body_search': body_search,
                                                      'title_search': title_search,
                                                      })