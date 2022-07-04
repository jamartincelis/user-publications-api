from django.test import TestCase, Client
from rest_framework import status
from weather.models import City
from django.urls import reverse
from json import dumps

class WeatherTestCase(TestCase):

    client = Client()
    fixtures = [
        'weather/fixtures/cities.yaml'
    ]

    def test_get_all_cities(self):
        response = self.client.get(reverse('list_create'))
        data = response.json()
        cities = City.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data), cities.count())

    def test_create_city(self):
        payload = {
            "name": "Arica"      
        }
        response = self.client.post(
            reverse('list_create'),
            data=dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_city(self):
        payload = {
            "name": "XXXX"      
        }
        response = self.client.post(
            reverse('list_create'),
            data=dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)