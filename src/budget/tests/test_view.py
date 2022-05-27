from json import dumps

import pendulum

from django.test import TestCase, Client

from rest_framework import status

from budget.models import Budget


class BudgetsTestCase(TestCase):

    client = Client()
    fixtures = [
        'catalog/fixtures/catalogs.yaml',
        'catalog/fixtures/expenses_categories.yaml',
        'catalog/fixtures/incomes_categories.yaml',
        'catalog/fixtures/budget_status.yaml',
        'budget/fixtures/budgets.yaml'
    ]
    BASE_URL = '/users/c9d29378-f4d6-46ca-9363-1d304e9fa133/budgets/'
    BUDGET_DETAIL = BASE_URL + '45a80dbb-ea71-4ce3-90b3-6761bcbf365c/'
    BUDGET_CATEGORY = BASE_URL + 'categories/9abd4759-ab14-4e09-adc2-9c5dea1041b1/' # entretenimiento
    DATE_MONTH = '?date_month={}'

    @property
    def current_month(self):
        return '{}-{}'.format(pendulum.now().year, pendulum.now().month)

    @property
    def previous_month(self):
        return '{}-{}'.format(pendulum.now().year, pendulum.now().month)

    def update_budgets_dates(self):
        Budget.objects.all().update(budget_date='{}-01'.format(self.current_month))

    def test_get_user_budgets_by_month(self):
        self.update_budgets_dates()
        response = self.client.get(self.BASE_URL+self.DATE_MONTH.format(self.current_month))
        # print(dumps(response.json(), indent=4))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_budget_detail(self):
        response = self.client.get(self.BUDGET_DETAIL)
        # print(dumps(response.json(), indent=4))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_budget_status(self):
        body = {
            'status': 'f1ba1236-b4fd-4ed6-9d35-8114ed66726f' # eliminado
        }
        response = self.client.patch(self.BUDGET_DETAIL, data=body, content_type='application/json')
        # print(dumps(response.json(), indent=4))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_budget_amount(self):
        body = {
            'amount': 100.0
        }
        response = self.client.patch(self.BUDGET_DETAIL, data=body, content_type='application/json')
        # print(dumps(response.json(), indent=4))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_budgets_by_month_and_category(self):
        response = self.client.get(self.BUDGET_CATEGORY+self.DATE_MONTH.format(self.current_month))
        # print(dumps(response.json(), indent=4))
        self.assertEqual(response.status_code, status.HTTP_200_OK)