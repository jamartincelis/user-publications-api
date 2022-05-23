from django.test import TestCase
from django.urls import reverse
import tip.tests.constants as constants

class TestTipAppUrls(TestCase):
    def test_resolution_for_budget_list(self):
        self.assertEqual(reverse('tip:list'), constants.URL_TIP)