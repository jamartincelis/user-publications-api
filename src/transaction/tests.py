from json import dumps

import pendulum

from django.test import TestCase, Client

from rest_framework import status

from budget.models import Budget

from transaction.models import Transaction


class TransactionsTestCase(TestCase):

    client = Client()
    fixtures = [
        'catalog/fixtures/catalogs.yaml',
        'catalog/fixtures/account_types.yaml',
        'catalog/fixtures/expenses_categories.yaml',
        'catalog/fixtures/incomes_categories.yaml',
        'catalog/fixtures/budget_status.yaml',
        'budget/fixtures/budgets.yaml',
        'transaction/fixtures/transactions.yaml',
    ]

    BASE_URL = '/users/c9d29378-f4d6-46ca-9363-1d304e9fa133/transactions/'
    EXPENSES_SUMMARY_URL = BASE_URL + 'expenses/summary/'
    DATE_MONTH = '?date_month={}'

    @property
    def current_month(self):
        date = pendulum.now()
        return '{}-{}'.format(date.year, date.month)

    @property
    def previous_month(self):
        date = pendulum.now().subtract(months=1)
        return '{}-{}'.format(date.year, date.month)

    def update_transactions_date(self):
        Transaction.objects.all().update(transaction_date='{}-01'.format(self.current_month))

    def test_get_transactions_by_month(self):
        self.update_transactions_date()
        response = self.client.get(self.BASE_URL+self.DATE_MONTH.format(self.current_month))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
        # print(dumps(response.json(), indent=4))
        Transaction.objects.all().update(transaction_date='{}-01'.format(self.previous_month))
        response = self.client.get(self.BASE_URL+self.DATE_MONTH.format(self.current_month))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 0)

    def test_get_expenses_summary_by_month(self):
        Budget.objects.all().update(budget_date='{}-01'.format(self.current_month))
        Transaction.objects.all().update(transaction_date='{}-01'.format(self.current_month))
        response = self.client.get(self.EXPENSES_SUMMARY_URL+self.DATE_MONTH.format(self.current_month))
        print(dumps(response.json(), indent=4))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(0, 0)
