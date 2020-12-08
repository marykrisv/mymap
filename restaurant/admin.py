from django.contrib import admin
from . models import Restaurant, RestaurantType

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(RestaurantType)