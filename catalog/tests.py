import json

from django.test import TestCase, Client

from catalog.models import CodeType, Code


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
        # print(response.json())
        self.assertEqual(Code.objects.all().count(), len(response.json()))

    def test_list_all_catalogs(self):
        response = self.client.get('/catalog/list/')
        self.assertEqual(CodeType.objects.all().count(), len(response.json()))

    def test_filter_catalogs_by_name(self):
        response = self.client.get('/catalog/project_categories/')
        data = response.json()
        # print(json.dumps(data, indent=2, ensure_ascii=False))
        self.assertEqual(response.json()['name'], 'project_categories')
