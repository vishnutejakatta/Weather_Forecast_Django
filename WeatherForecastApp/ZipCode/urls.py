from django.urls import path
from . import views
urlpatterns = [
    path('', views.get_zipcode_weather, name='zipcode_weather'),
]