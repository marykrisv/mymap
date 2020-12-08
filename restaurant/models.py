from django.db import models

# Create your models here.
class RestaurantType(models.Model):
    name = models.CharField(default="", max_length=200)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(default="", max_length=200)
    lat = models.DecimalField(max_digits=25, decimal_places=20)
    lng = models.DecimalField(max_digits=25, decimal_places=20)
    customer_visits = models.IntegerField()
    food_specialty = models.CharField(max_length=200)
    restaurant_type = models.ForeignKey(RestaurantType, on_delete=models.CASCADE)
    patrons = models.CharField(blank=True, max_length=200)
    revenue = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return self.name