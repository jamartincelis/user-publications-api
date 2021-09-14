from django.test import TestCase, Client
from transaction.models import Transaction
from json import dumps
from rest_framework import status

class BudgetTestCase(TestCase):

    client = Client()
    fixtures = [
        'user/fixtures/users.yaml',
        'catalog/fixtures/codetype.yaml',
        'catalog/fixtures/transactions_categories.yaml',
        'transaction/fixtures/transactions.yaml'
    ]
    DATE_MONTH = "?date_month={}"
    URL_BASE = '/user/{}/transactions/'
    URL_DETAIL = URL_BASE + '{}/'
    URL_CATEGORY = URL_BASE + 'categories/{}/' + DATE_MONTH
    URL_DATE_MONTH = URL_BASE + DATE_MONTH

    def test_budgets_without_date_month_param(self):
        user_id = '0390a508-dba5-4344-b77f-93e1227d42f4'
        response = self.client.get(self.URL_BASE.format(user_id))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'400': "date_month it's required."}
        )        

    def invalid_date_month_param_base(self,date_month):
        user_id = '0390a508-dba5-4344-b77f-93e1227d42f4'
        response = self.client.get((self.URL_DATE_MONTH).format(user_id,date_month))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'400': 'Invalid date format.'}
        )
          
    def test_invalid_date_month_param_1(self):
        date_month = "2021-13"
        self.invalid_date_month_param_base(date_month)

    def test_invalid_date_month_param_2(self):
        date_month = "12-2021"
        self.invalid_date_month_param_base(date_month)

    def test_transactions_list_by_date(self):
        user_id = '0390a508-dba5-4344-b77f-93e1227d42f4'
        transactions = Transaction.objects.filter(user=user_id,
            transaction_date__range=['2021-09-01', '2021-09-30']
        )
        date_month = "2021-09"
        response = self.client.get(self.URL_DATE_MONTH.format(user_id,date_month))
        data = response.json()
        self.assertEqual(transactions.count(), len(data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_transaction_detail(self):
        user_id = '479ec168013945d0b7042bc4e5d0c4fb'
        transaction_id = '68e18783-8b51-4618-af83-50c77f25871d'
        transaction = Transaction.objects.get(user=user_id,id=transaction_id)
        response = self.client.get(self.URL_DETAIL.format(user_id,transaction_id))
        data = response.json()
        self.assertEqual(data['id'], str(transaction.id))
        self.assertEqual(data['user'], str(transaction.user.id))
        self.assertEqual(data['category'], str(transaction.category.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_transactions_list_by_date_and_category(self):
        user_id = '0390a508-dba5-4344-b77f-93e1227d42f4'
        category_id = '22118f55-e6a9-46b0-ae8f-a063dda396e0' #Shopping
        date_month = "2021-09"
        transactions = Transaction.objects.filter(user=user_id,
            transaction_date__range=['2021-09-01', '2021-09-30'],
            category = category_id
        )
        response = self.client.get(self.URL_CATEGORY.format(user_id, category_id, date_month))
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(transactions.count(), len(data))

    def test_add_note_to_transaction(self):
        user_id = '0390a508-dba5-4344-b77f-93e1227d42f4'
        transactions_id = '68e18783-8b51-4618-af83-50c77f25871d'
        user_note = "Transaccion de prueba 3"
        payload = {"user_note" : user_note}
        response = self.client.patch(
            self.URL_DETAIL.format(user_id, transactions_id),
            data=dumps(payload),
            content_type='application/json'            
        )
        response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['user_note'], user_note)

    def test_add_category_to_transaction(self):
        user_id = '0390a508-dba5-4344-b77f-93e1227d42f4'
        transactions_id = '68e18783-8b51-4618-af83-50c77f25871d'
        category_id = "22118f55-e6a9-46b0-ae8f-a063dda396e0"
        payload = {"category" : category_id}
        response = self.client.patch(
            self.URL_DETAIL.format(user_id, transactions_id),
            data=dumps(payload),
            content_type='application/json'            
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['category'], category_id)