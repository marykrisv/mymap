from django.shortcuts import render
from django.conf import settings
from .models import Restaurant, RestaurantType
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.forms.models import model_to_dict
from django.db.models import Count, Sum
from django.core import serializers

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

@csrf_exempt
def addCustomerVisit(request):
      id = request.POST["id"]

      currVisits = Restaurant.objects.filter(id=id).first().customer_visits

      Restaurant.objects.filter(id = id).update(customer_visits=(currVisits+1))

      return HttpResponse("OK")

@csrf_exempt
def getRestaurantTypeCustPercentage(request):
      resTypeByVisit = getVisitsByResType()
      resTypePercentages = []

      total = resTypeByVisit['total']
      details = resTypeByVisit['details']

      for res in details:
            resTypePercentage = {
                  'y': round(res['total'] / total * 100, 2),
                  'label': RestaurantType.objects.filter(id=res['restaurant_type']).first().name
            }
            resTypePercentages.append(resTypePercentage)

      return HttpResponse(json.dumps(resTypePercentages))

def getVisitsByResType():
      ret = {}
      resTypes = Restaurant.objects.values('restaurant_type').annotate(total=Sum('customer_visits')).order_by('total')
      total = 0

      # get total first
      for res in resTypes:
            total = total + res['total']

      ret['total'] = total
      ret['details'] = resTypes

      return ret

@csrf_exempt
def getRestaurantTypeRevenuPercentage(request):
      resTypeByRev = getRevenueByResType()
      resTypePercentages = []

      total = resTypeByRev['total']
      details = resTypeByRev['details']

      for res in details:
            resTypePercentage = {
                  'y': round(res['total'] / total * 100, 2),
                  'label': RestaurantType.objects.filter(id=res['restaurant_type']).first().name
            }
            resTypePercentages.append(resTypePercentage)

      return HttpResponse(json.dumps(resTypePercentages))

def getRevenueByResType():
      ret = {}
      resTypes = Restaurant.objects.values('restaurant_type').annotate(total=Sum('revenue')).order_by('total')
      total = 0

      # get total first
      for res in resTypes:
            total = total + res['total']

      ret['total'] = total
      ret['details'] = resTypes

      return ret

@csrf_exempt
def getTopRestaurantWithVisit(request):
      result = Restaurant.objects.all().order_by('-customer_visits')[:5]

      topResVisits = []

      for res in result:
            rest = {
                  'name': res.name,
                  'type': res.restaurant_type.name,
                  'visits': res.customer_visits
            }
            topResVisits.append(rest)

      return HttpResponse(json.dumps(topResVisits))

@csrf_exempt
def getTopRestaurantWithRevenue(request):
      result = Restaurant.objects.all().order_by('-revenue')[:5]

      topResRevenue = []

      for res in result:
            rest = {
                  'name': res.name,
                  'type': res.restaurant_type.name,
                  'revenue': res.revenue
            }
            topResRevenue.append(rest)

      return HttpResponse(json.dumps(topResRevenue))