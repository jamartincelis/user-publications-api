from json import dumps

from django.test import TestCase, Client

from rest_framework import status

from catalog.models import Catalog


class CatalogTestCase(TestCase):

    client = Client()
    fixtures = [
        'catalog/fixtures/catalogs.yaml',
        'catalog/fixtures/expenses_categories.yaml',
        'catalog/fixtures/incomes_categories.yaml',
        'catalog/fixtures/budget_status.yaml',
    ]
    BASE_URL = '/pfm-service/catalogs/'

    def test_get_all_catalogs(self):
        response = self.client.get(self.BASE_URL + 'all/')
        # print(dumps(response.json(), indent=4))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_specific_catalogs(self):
        response = self.client.get(self.BASE_URL + '?catalog=incomes_categories')
        # print(dumps(response.json(), indent=4))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_specific_item(self):
        response = self.client.get(self.BASE_URL + 'items/53566d37-4b4d-4598-8b6c-09f5970c33cd/')
        # print(dumps(response.json(), indent=4))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
