from django.contrib import admin
from .models import Restaurant
from .models import Food
from .models import Order

admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Order)
