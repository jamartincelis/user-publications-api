import json

from django.test import TestCase, Client
from catalog.models import CodeType, Code
from rest_framework import status

class CatalogsTestCase(TestCase):

    client = Client()
    fixtures = [
        'catalog/fixtures/codetype.yaml'
    ]

    def test_list_all_code_types(self):
        response = self.client.get('/catalog/codetypes_list/')
        self.assertEqual(CodeType.objects.all().count(), len(response.json()))

    def test_list_all_codes(self):
        response = self.client.get('/catalog/codes_list/')
        self.assertEqual(Code.objects.all().count(), len(response.json()))

    def test_list_all_catalogs(self):
        response = self.client.get('/catalog/list/')
        self.assertEqual(CodeType.objects.all().count(), len(response.json()))

    def test_filter_catalogs_by_name_account_status(self):
        response = self.client.get('/catalog/account_status/')
        data = response.json()
        code_type = CodeType.objects.get(name="account_status")
        self.assertEqual(data['name'], code_type.name)
        self.assertEqual(data['id'], str(code_type.id))
        
    def test_filter_catalogs_by_name_incomes_category(self):
        response = self.client.get('/catalog/incomes_categories/')
        data = response.json()
        code_type = CodeType.objects.get(name="incomes_categories")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['name'], code_type.name)
        self.assertEqual(data['id'], str(code_type.id))

    def test_filter_catalogs_by_name_expenses_category(self):
        response = self.client.get('/catalog/expenses_categories/')
        data = response.json()
        code_type = CodeType.objects.get(name="expenses_categories")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['name'], code_type.name)
        self.assertEqual(data['id'], str(code_type.id))

    def test_filter_catalogs_by_name_account_type(self):
        response = self.client.get('/catalog/account_type/')
        data = response.json()
        code_type = CodeType.objects.get(name="account_type")
        self.assertEqual(data['name'], code_type.name)
        self.assertEqual(data['id'], str(code_type.id))
