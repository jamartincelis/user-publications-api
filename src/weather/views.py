from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

from weather.serializers import City, CitySerializer
from weather.models import City


class WeatherList(ListCreateAPIView):
    """
    Devuelve la lista de ciudades
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer