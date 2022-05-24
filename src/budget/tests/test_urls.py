from django.test import TestCase
from django.urls import reverse
import budget.tests.constants as constants

class TestBudgetAppUrls(TestCase):
    USER_ID = constants.USER_ID
    BUDGET_ID = constants.BUDGET_ID

    def test_resolution_for_budget_list(self):        
        url = reverse('budget:list',kwargs={'user':self.USER_ID})
        self.assertEqual(url, constants.URL_BUDGET.format(self.USER_ID))

    def test_resolution_for_budget_detail(self):        
        url = reverse('budget:detail',kwargs={'user':self.USER_ID, 'pk': self.BUDGET_ID})
        self.assertEqual(url, constants.URL_DETAIL.format(self.USER_ID, self.BUDGET_ID))