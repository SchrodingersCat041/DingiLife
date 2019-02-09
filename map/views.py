from django.shortcuts import render, HttpResponse
from .models import NearBy



def home_view(request):
    return render(request, 'map/vallagena.html')


def restaurant_view(request):
    restaurants = NearBy.objects.raw("SELECT id,name FROM map_nearby where place_type = 'restaurant'")
    return render(request, 'map/nearby_list.html',
                  {'restaurants': restaurants, 'place_type': 'restaurant'})


def shopping_mall_view(request):
    shopping_malls = NearBy.objects.raw("SELECT id,name FROM map_nearby where place_type = 'shopping mall'")
    return render(request, 'map/nearby_list.html',
                  {'shopping_malls': shopping_malls, 'place_type': 'shopping mall'})
