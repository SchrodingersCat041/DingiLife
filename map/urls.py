from django.urls import path
from . import views

app_name = 'map'

urlpatterns = [
    path('home/', views.home_view, name='home_view'),
    path('restaurant/', views.restaurant_view, name='restaurant_view'),
    path('shopping_malls/', views.shopping_mall_view, name='shopping_mall_view')
]