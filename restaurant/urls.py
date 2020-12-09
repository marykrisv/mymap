from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('filter-restaurants', views.filterRestaurants, name='filter'),    
    path('add-customer-visit', views.addCustomerVisit),
    path('get-restaurant-type-cust-with-percentage', views.getRestaurantTypeCustPercentage),
    path('get-restaurant-type-rev-with-percentage', views.getRestaurantTypeRevenuPercentage),
    path('get-top-restaurant-with-visits', views.getTopRestaurantWithVisit),
    path('get-top-restaurant-with-revenue', views.getTopRestaurantWithRevenue)
]