from django.urls import path
from weather.views import WeatherList

urlpatterns = [
    path('cities', WeatherList.as_view(), name="list_create"),
]
