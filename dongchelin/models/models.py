from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 

class Restaurant(models.Model):
	objects = models.Manager()
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	favo = models.ManyToManyField(User, related_name='favo')

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Food(models.Model):
	objects = models.Manager()
	name = models.CharField(max_length=100)
	price = models.IntegerField(validators=[MinValueValidator(1)])
	image = models.ImageField(upload_to = "static/img/", null = True)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="foods")

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
	objects = models.Manager()
	status = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="order")
	total_price = models.IntegerField(default=0)
	detail = models.TextField(default="")

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


