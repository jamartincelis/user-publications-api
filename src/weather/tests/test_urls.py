from django.test import TestCase
from django.urls import reverse
from weather import MODULE_SETTINGS

class TestWeatherUrls(TestCase):
    def test_resolution_for_list_create(self):
        url = reverse('list_create')
        self.assertEqual(url, MODULE_SETTINGS['URL_CITY_LIST_CREATE'])