from django.shortcuts import render,redirect
from .models import Food,Consume
# Create your views here.

def foodView(request):
    if request.method == 'POST':
        food_consume = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consume)
        user = request.user
        consumed = Consume(user=user,food_consume=consume)
        consumed.save()
        food = Food.objects.all()
    else:
        food = Food.objects.all()
    consumed_food =Consume.objects.filter(user=request.user)
    return render(request,'Food/index.html',{'food':food,'consumed_food':consumed_food})

def remove(request,id):
    food_consume = Consume.objects.get(id=id)
    if request.method == 'POST':
        food_consume.delete()
        return redirect('/')

    return render(request,'Food/delete.html')