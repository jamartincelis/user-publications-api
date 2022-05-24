from django.test import TestCase
from django.urls import reverse
import faq.tests.constants as constants

class TestFaqAppUrls(TestCase):
    def test_resolution_for_budget_list(self):
        self.assertEqual(reverse('faq:list'), constants.URL_FAQ)