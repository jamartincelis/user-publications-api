from json import dumps
from django.test import TestCase, Client
from faq.models import Faq
from rest_framework import status

class BudgetTestCase(TestCase):

    client = Client()
    fixtures = [
        'faq/fixtures/faqs.yaml',
    ]
    URL_BASE = '/faqs/'

    def test_faqs_list(self):
        faqs = Faq.objects.filter()
        response = self.client.get(self.URL_BASE)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(faqs.count(), len(data))