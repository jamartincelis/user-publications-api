from django.test import TestCase
from django.urls import reverse
import monitoring.tests.constants as constants

class TestMonitoringAppUrls(TestCase):
    def test_resolution_for_health_check(self):        
        url = reverse('health-check')
        self.assertEqual(url, constants.URL_MONITORING.format('health-check'))

    def test_resolution_for_sentry(self):
        url = reverse('sentry')
        self.assertEqual(url, constants.URL_MONITORING.format('sentry'))