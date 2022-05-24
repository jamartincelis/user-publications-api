from json import dumps
from django.test import TestCase, Client
from rest_framework import status
from transaction.models import Transaction
from django.urls import reverse
from django.utils.http import urlencode
import transaction.tests.constants as constants

class TransactionsTestCase(TestCase):

    client = Client()
    fixtures = [
        'transaction/fixtures/transactions.yaml'
    ]
    USER_ID = 'b9e605ee-4cca-400e-99c5-ae24abca97d5'
    
    def test_budgets_without_date_month_param(self):
        user_id = '0390a508-dba5-4344-b77f-93e1227d42f4'

        response = self.client.get(reverse(constants.URL_TRANSACTION_LIST,kwargs={'user':user_id}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'400': "Invalid date format."})

    def invalid_date_month_param_base(self,date_month):
        """
        Funcion base para las pruebas 
        """
        query_kwargs={'date_month': date_month}
        url = '{}?{}'.format(
            reverse(constants.URL_TRANSACTION_LIST,kwargs={'user':self.USER_ID}), 
            urlencode(query_kwargs)
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        return self.assertJSONEqual(str(response.content, encoding='utf8'), {'400': 'Invalid date format.'})

    def test_invalid_date_month_param_1(self):
        date_month = "2021-13"
        self.invalid_date_month_param_base(date_month)

    def test_invalid_date_month_param_2(self):
        date_month = "12-2021"
        self.invalid_date_month_param_base(date_month)

    def test_get_transaction_detail(self):
        transactions_id = "203a1ace-8a57-4d49-ae8d-699221e9f3cb"
        response = self.client.get(
            reverse(constants.URL_TRANSACTION_DETAIL,kwargs={'user':self.USER_ID, 'pk': transactions_id}),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_transactions_list_by_date(self):
        query_kwargs={'date_month': '2021-09'}
        url = '{}?{}'.format(reverse(constants.URL_TRANSACTION_LIST,kwargs={'user':self.USER_ID}), urlencode(query_kwargs))

        transactions = Transaction.objects.filter(user=self.USER_ID,
            transaction_date__range=['2021-09-01', '2021-09-30'])
        response = self.client.get(url)
        
        data = response.json()
        self.assertEqual(transactions.count(), len(data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_note_to_transaction(self):
        transactions_id = '68e18783-8b51-4618-af83-50c77f25871d'
        user_note = 'Esta es una nota'
        payload = {
            'user_note' : user_note
        }
        response = self.client.patch(
            reverse(constants.URL_TRANSACTION_DETAIL,kwargs={'user':self.USER_ID, 'pk': transactions_id}),
            data=dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['user_note'], user_note)

    def test_add_category_to_transaction(self):
        transactions_id = '72ad54c2-e3cd-4a11-86e3-767f34728a04'
        category_id = '9abd4759-ab14-4e09-adc2-9c5dea1041b1'
        payload = {'category' : category_id}

        response = self.client.patch(
            reverse(constants.URL_TRANSACTION_DETAIL,kwargs={'user':self.USER_ID, 'pk': transactions_id}),
            data=dumps(payload),
            content_type='application/json'            
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ExpensesSummaryTestCase(TestCase):

    client = Client()
    fixtures = [
        'transaction/fixtures/transactions.yaml'
    ]

    USER_ID = '0390a508-dba5-4344-b77f-93e1227d42f4'

    def test_get_expenses_summary_by_month(self):

        query_kwargs={'date_month': '2021-09'}
        url = '{}?{}'.format(
            reverse('transaction:expenses_summary',kwargs={'user':self.USER_ID}), 
            urlencode(query_kwargs)
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
