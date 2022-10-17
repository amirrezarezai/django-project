from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    products_object = Products.objects.all()
    #search
    search_item = request.GET.get('item_name')
    if search_item != '' and search_item is not None:
        products_object = Products.objects.filter(title__icontains=search_item)
    #pagination
    paginator = Paginator(products_object,4)
    page_number = request.GET.get('page')
    products_object = paginator.get_page(page_number)

    return render(request,'shop/index.html',{'products_object':products_object})


def detail(request,id):
    product_object = Products.objects.get(id=id)
    return render(request,'shop/detail.html',{'product_object':product_object})

def checkout(request):
    return render(request,'shop/checkout.html')