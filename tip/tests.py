from django.test import TestCase, Client
from tip.models import Tip
from rest_framework import status

class TipTestCase(TestCase):

    client = Client()
    fixtures = [
        'tip/fixtures/tips.yaml',
    ]
    URL_BASE = '/tips/'

    def test_tip_list(self):
        tips = Tip.objects.filter()
        response = self.client.get(self.URL_BASE)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(tips.count(), len(data))