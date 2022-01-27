from django.test import TestCase, Client
from notification.models import Notification
from rest_framework import status

class NotificationTestCase(TestCase):

    client = Client()
    fixtures = [
        'notification/fixtures/notifications.yaml',
    ]
    URL_BASE = '/notifications/'

    def test_notification_list(self):
        notifications = Notification.objects.all()
        response = self.client.get(self.URL_BASE)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(notifications.count(), len(data))