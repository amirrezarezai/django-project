from django.shortcuts import render,redirect
from .models import Contacts
# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_id = request.POST['user_id']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contacts(car_id=car_id,car_title=car_title,
                           first_name=first_name,last_name=last_name,
                           user_id=user_id,customer_need=customer_need,city=city,
                           state=state,email=email,phone=phone,message=message)
        contact.save()
        return redirect('cars:cars')
