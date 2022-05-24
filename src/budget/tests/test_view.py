from json import dumps
from django.test import TestCase, Client
from budget.models import Budget
from rest_framework import status
from django.urls import reverse
from django.utils.http import urlencode
import budget.tests.constants as constants

class BudgetTestCase(TestCase):

    client = Client()
    fixtures = [
        'budget/fixtures/budgets.yaml'
    ]

    USER_ID = constants.USER_ID
    BUDGET_ID = constants.BUDGET_ID

    def test_budgets_list(self):
        budgets = Budget.objects.filter(user=self.USER_ID,
            budget_date__range=['2021-09-01', '2021-09-30']
        )
        date_month = "2021-09"
        query_kwargs={'date_month': date_month}
        url = '{}?{}'.format(
            reverse(constants.URL_BUDGET_LIST,kwargs={'user':self.USER_ID}), 
            urlencode(query_kwargs)
        )        
        response = self.client.get(url)

        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(budgets.count(), len(data))

    def test_budget_detail(self):
        budget = Budget.objects.get(user=self.USER_ID,id=self.BUDGET_ID)
        url = reverse(constants.URL_BUDGET_DETAIL,kwargs={'user':self.USER_ID, 'pk': self.BUDGET_ID})

        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['id'], str(budget.id))
        self.assertEqual(data['user'], str(budget.user))
        self.assertEqual(data['category']['id'], str(budget.category))

    def test_add_budget(self):
        payload = {
            "amount": 3000,
            "budget_date": "2021-09-09T15:20:30-04:00",
            "user": "479ec168-0139-45d0-b704-2bc4e5d0c4fb",
            "category": "22118f55-e6a9-46b0-ae8f-a063dda396e0"
        }
        response = self.client.post(
            reverse(constants.URL_BUDGET_LIST,kwargs={'user':self.USER_ID}),
            data=dumps(payload),
            content_type='application/json'            
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)