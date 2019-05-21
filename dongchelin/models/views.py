from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant
from .models import Food
from .models import Order
from django.contrib.auth.models import User

def main(request):
	restaurants = Restaurant.objects.all()
	return render(request, 'models/main.html', {"restaurants": restaurants})


def restaurant(request, id):
	restaurant = get_object_or_404(Restaurant, pk=id)
	return render(request, 'models/restaurant.html', {"restaurant": restaurant})


def make_order(request, id):
	restaurant = get_object_or_404(Restaurant, pk=id)
	if request.method == "POST":
		total_price = 0
		detail = ""
		for item in restaurant.foods.all():
			if int(request.POST[item.name], base=10) != 0:
				print("=========="+item.name)
				print(item.price)
				print("=========="+request.POST[item.name])
				detail += item.name + "("+ str(item.price) +") X " + request.POST[item.name] + "\n"
				print(detail)
				total_price += item.price * int(request.POST[item.name], base=10)
				print(total_price)
		order = Order(total_price=total_price, detail=detail, user=request.user, restaurant=restaurant)
		order.save()
		return redirect('show_order', order.id)
	return render(request, 'models/show_order.html', {"order": order})
		

def show_order(request, id):
	order = get_object_or_404(Order, pk=id)
	return render(request, 'models/show_order.html', {"order": order})


def order_list(request):
	orders = Order.objects.filter(
		user = request.user
	)
	return render(request, 'models//order_list.html', {"orders": orders})

