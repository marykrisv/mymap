from django.shortcuts import render
from django.conf import settings
from .models import Restaurant, RestaurantType
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.forms.models import model_to_dict

# Create your views here.
def index(request):
      restaurant_types = RestaurantType.objects.all()

      context = {
            "center": settings.CEBU_LOC,
            "api_key": settings.MAP_API_KEY,
            "map_zoom": settings.MAP_ZOOM,
            'restaurant_types': restaurant_types
      }
      return render(request, 'showRestaurants.html', context)

@csrf_exempt
def filterRestaurants(request):
      res_type = request.POST["type"]

      if (res_type == 'all'):
            restaurants = Restaurant.objects.all()
      else:
            restaurants = Restaurant.objects.filter(restaurant_type=res_type)

      restaurant_dict = []

      for res in restaurants:
            res_dict = model_to_dict(res)
            res_dict['lat'] = str(res.lat)
            res_dict['lng'] = str(res.lng)
            res_dict['restaurant_type_name'] = res.restaurant_type.name
            restaurant_dict.append(res_dict)

      return HttpResponse(json.dumps(restaurant_dict))