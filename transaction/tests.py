from json import dumps

from django.test import TestCase, Client

from rest_framework import status

from transaction.models import Transaction


class TransactionsTestCase(TestCase):

    client = Client()
    fixtures = [
        'catalog/fixtures/codetype.yaml',
        'catalog/fixtures/accounts_types.yaml',
        'catalog/fixtures/transactions_categories.yaml',
        'user/fixtures/users.yaml',
        'account/fixtures/accounts.yaml',
        'transaction/fixtures/transactions.yaml',
        'transaction/fixtures/monthly_summaries.yaml'
    ]
    DATE_MONTH = "?date_month={}"
    YEAR = "?year={}"
    URL_BASE = '/user/{}/transactions/'
    URL_DETAIL = URL_BASE + '{}/'
    URL_CATEGORY = URL_BASE + 'categories/{}/' + DATE_MONTH
    URL_EXPENSES = URL_BASE + 'expenses/summary/' + DATE_MONTH
    URL_BALANCE = URL_BASE + 'balance/' + YEAR
    URL_DATE_MONTH = URL_BASE + DATE_MONTH
    USER = '0390a508-dba5-4344-b77f-93e1227d42f4'
    CATEGORY = '22118f55-e6a9-46b0-ae8f-a063dda396e0'

    def test_budgets_without_date_month_param(self):
        user_id = '0390a508-dba5-4344-b77f-93e1227d42f4'
        response = self.client.get(self.URL_BASE.format(user_id))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'400': "Invalid date format."})

    def invalid_date_month_param_base(self,date_month):
        """
        Funcion base para las pruebas 
        """
        response = self.client.get((self.URL_DATE_MONTH).format(self.USER,date_month))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        return self.assertJSONEqual(str(response.content, encoding='utf8'), {'400': 'Invalid date format.'})

    def test_invalid_date_month_param_1(self):
        date_month = "2021-13"
        self.invalid_date_month_param_base(date_month)

    def test_invalid_date_month_param_2(self):
        date_month = "12-2021"
        self.invalid_date_month_param_base(date_month)

    def test_get_transaction_detail(self):
        response = self.client.get(self.URL_DETAIL.format(self.USER, '203a1ace-8a57-4d49-ae8d-699221e9f3cb'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_transactions_list_by_date(self):
        transactions = Transaction.objects.filter(account__user=self.USER,
            transaction_date__range=['2021-09-01', '2021-09-30'])
        response = self.client.get(self.URL_DATE_MONTH.format(self.USER, '2021-09'))
        data = response.json()
        self.assertEqual(transactions.count(), len(data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_note_to_transaction(self):
        transaction = '68e18783-8b51-4618-af83-50c77f25871d'
        user_note = 'Esta es una nota'
        payload = {
            'user_note' : user_note
        }
        response = self.client.patch(
            self.URL_DETAIL.format(self.USER, transaction),
            data=dumps(payload),
            content_type='application/json'
        )
        # print(dumps(response.json(), indent=4, ensure_ascii=False))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['user_note'], user_note)

    def test_add_category_to_transaction(self):
        user_id = '0390a508-dba5-4344-b77f-93e1227d42f4'
        transactions_id = '68e18783-8b51-4618-af83-50c77f25871d'
        category_id = '22118f55-e6a9-46b0-ae8f-a063dda396e0'
        payload = {'category' : category_id}
        response = self.client.patch(
            self.URL_DETAIL.format(user_id, transactions_id),
            data=dumps(payload),
            content_type='application/json'            
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['category']['id'], category_id)


class ExpensesSummaryTestCase(TestCase):

    client = Client()
    fixtures = [
        'catalog/fixtures/codetype.yaml',
        'catalog/fixtures/accounts_types.yaml',
        'catalog/fixtures/transactions_categories.yaml',
        'user/fixtures/users.yaml',
        'account/fixtures/accounts.yaml',
        'transaction/fixtures/expenses_summary.yaml'
    ]
    USER = '0390a508-dba5-4344-b77f-93e1227d42f4'
    CATEGORY = '22118f55-e6a9-46b0-ae8f-a063dda396e0'
    URL = '/user/{}/transactions/expenses/summary/?date_month={}'

    def test_get_expenses_summary_by_month(self):
        response = self.client.get(self.URL.format(self.USER, '2021-09'))
        # print(dumps(response.json(), indent=4, ensure_ascii=False))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
