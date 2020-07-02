from django.urls import path
from . import views
urlpatterns = [
    path('', views.get_city_weather, name="city_weather"),
]