from django.urls import path
from . import views


urlpatterns = [
	path('main/', views.main, name="main"),
	path('restaurant/<int:id>/', views.restaurant, name="restaurant"),
	path('make_order/<int:id>/', views.make_order, name="make_order"),
	path('show_order/<int:id>/', views.show_order, name="show_order"),
	path('order_list/', views.order_list, name="order_list"),
	path('<int:id>/favo/', views.favo, name="favo"),
	path('favo_list/', views.favo_list, name="favo_list"),
]
