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
    TRANSACTION_DETAIL = BASE_URL + '0b0588dc-2020-4bac-a18f-52979efb41c2/'
    TRANSACTIONS_BY_MONTH_AND_CATEGORY = BASE_URL + 'summary/'
    MONTHLY_BALANCE = BASE_URL + 'balance/'
    MONTHLY_BALANCE_BY_CATEGORY = BASE_URL + 'balance/category/22118f55-e6a9-46b0-ae8f-a063dda396e0/'
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
        self.assertEqual(len(response.json()), 2)
        # print(dumps(response.json(), indent=4))
        Transaction.objects.all().update(transaction_date='{}-01'.format(self.previous_month))
        response = self.client.get(self.BASE_URL+self.DATE_MONTH.format(self.current_month))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 0)

    def test_get_expenses_summary_by_month(self):
        Budget.objects.all().update(budget_date='{}-01'.format(self.current_month))
        Transaction.objects.all().update(transaction_date='{}-01'.format(self.current_month))
        response = self.client.get(self.EXPENSES_SUMMARY_URL+self.DATE_MONTH.format(self.current_month))
        # print(dumps(response.json(), indent=4))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_transaction_detail(self):
        response = self.client.get(self.TRANSACTION_DETAIL)
        # print(dumps(response.json(), indent=4))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_transaction_category(self):
        body = {
            'category': 'a249c468-bb4d-4365-83f4-108d456bb494' # Actualziar a Supermercados
        }
        response = self.client.patch(self.TRANSACTION_DETAIL, data=body, content_type='application/json')
        # print(dumps(response.json(), indent=4))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_transactions_by_category_and_month(self):
        Transaction.objects.all().update(transaction_date='{}-01'.format(self.current_month))
        response = self.client.get(self.TRANSACTIONS_BY_MONTH_AND_CATEGORY+self.DATE_MONTH.format(self.current_month))
        # print(dumps(response.json(), indent=4))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_monthly_balance(self):
        Transaction.objects.all().update(transaction_date='{}-01'.format(self.current_month))
        response = self.client.get(self.MONTHLY_BALANCE)
        # print(dumps(response.json(), indent=4))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_monthly_balance_by_category(self):
        Transaction.objects.all().update(transaction_date='{}-01'.format(self.current_month))
        response = self.client.get(self.MONTHLY_BALANCE_BY_CATEGORY+self.DATE_MONTH.format(self.current_month))
        # print(dumps(response.json(), indent=4))
        self.assertEqual(response.status_code, status.HTTP_200_OK)