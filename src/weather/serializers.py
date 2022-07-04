import requests
from rest_framework import serializers
from weather.models import City
from weather import MODULE_SETTINGS

class CitySerializer(serializers.ModelSerializer):
    """
    Permite acceder a lo datos basicos de una ciudad.
    """
    class Meta:
        model = City
        fields = '__all__'

    def validate(self, data):
        """
        Validar ciudades
        """
        url = MODULE_SETTINGS['OPEN_WEATHER_MAP_URL']
        response = requests.get(url.format(data['name'])).json()
        if response['cod'] == '404':
            raise serializers.ValidationError(response['message'])
        return data

    def to_representation(self, instance):
        """
        Permite modificar la forma en que se retornan las ciudades.
        """
        data = super(CitySerializer, self).to_representation(instance)

        url = MODULE_SETTINGS['OPEN_WEATHER_MAP_URL']
        response = requests.get(url.format(data['name'])).json()
        
        data.pop('id')
        data.pop('name')
        
        data['city'] = response['name'],
        data['temperature'] = response['main']['temp'],
        data['description'] = response['weather'][0]['main'],

        data.update(data)
        return data