from django.test import TestCase
from django.urls import reverse
import notification.tests.constants as constants

class TestNotificationAppUrls(TestCase):
    def test_resolution_for_notification_list(self):
        self.assertEqual(reverse('notification:list'), constants.URL_NOTIFICATION)