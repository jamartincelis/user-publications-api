from json import dumps

from django.test import TestCase, Client

from rest_framework import status

from notification.models import Notification


class NotificationTestCase(TestCase):

    client = Client()
    fixtures = [
        'notification/fixtures/notifications.yaml'
    ]
    BASE_URL = '/pfm-service/notifications/'

    def test_get_all_faqs(self):
        response = self.client.get(self.BASE_URL)
        # print(dumps(response.json(), indent=4))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
