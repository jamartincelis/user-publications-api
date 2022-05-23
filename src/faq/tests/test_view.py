from django.test import TestCase, Client
from faq.models import Faq
from rest_framework import status
from django.urls import reverse

class FaqTestCase(TestCase):

    client = Client()
    fixtures = [
        'faq/fixtures/faqs.yaml',
    ]

    def test_faqs_list(self):
        faqs = Faq.objects.filter()
        response = self.client.get(reverse('faq:list'))
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(faqs.count(), len(data))