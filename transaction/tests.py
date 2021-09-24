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
    BASE_URL = '/user/{}/transactions/'
    DATE_MONTH = '?date_month={}'
    DETAIL_URL = BASE_URL + '{}/'
    CATEGORY_URL = BASE_URL + 'categories/{}/' + DATE_MONTH
    DATE_MONTH_URL = BASE_URL + DATE_MONTH
    USER = '0390a508-dba5-4344-b77f-93e1227d42f4'
    CATEGORY = '22118f55-e6a9-46b0-ae8f-a063dda396e0'

    def test_get_users_transactions_for_a_given_month(self):
        response = self.client.get(self.DATE_MONTH_URL.format(self.USER, '2021-09'))
        # print(dumps(response.json(), indent=4, ensure_ascii=False))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_date_month_parameter(self):
        response = self.client.get((self.DATE_MONTH_URL).format(self.USER, '2021-a'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'400': 'Invalid date format.'})

    def test_get_transaction_detail(self):
        response = self.client.get(self.DETAIL_URL.format(self.USER, '203a1ace-8a57-4d49-ae8d-699221e9f3cb'))
        # print(dumps(response.json(), indent=4, ensure_ascii=False))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_transactions_list_by_date(self):
        transactions = Transaction.objects.filter(account__user=self.USER,
            transaction_date__range=['2021-09-01', '2021-09-30']
        )
        response = self.client.get(self.DATE_MONTH_URL.format(self.USER, '2021-09'))
        data = response.json()
        self.assertEqual(transactions.count(), len(data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
 
    def test_get_transactions_list_by_date_and_category(self):
        transactions = Transaction.objects.filter(account__user=self.USER,
            transaction_date__range=['2021-09-01', '2021-09-30'],
            category = self.CATEGORY
        )
        response = self.client.get(self.CATEGORY_URL.format(self.USER, self.CATEGORY, '2021-09'))
        data = response.json()
        # print(dumps(data, indent=4, ensure_ascii=False))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(transactions.count(), len(data))

    def test_add_note_to_transaction(self):
        transaction = '68e18783-8b51-4618-af83-50c77f25871d'
        user_note = 'Esta es una nota'
        payload = {
            'user_note' : user_note
        }
        response = self.client.patch(
            self.DETAIL_URL.format(self.USER, transaction),
            data=dumps(payload),
            content_type='application/json'            
        )
        # print(dumps(response.json(), indent=4, ensure_ascii=False))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['user_note'], user_note)

#     def test_add_category_to_transaction(self):
#         user_id = '0390a508-dba5-4344-b77f-93e1227d42f4'
#         transactions_id = '68e18783-8b51-4618-af83-50c77f25871d'
#         category_id = '22118f55-e6a9-46b0-ae8f-a063dda396e0'
#         payload = {'category' : category_id}
#         response = self.client.patch(
#             self.URL_DETAIL.format(user_id, transactions_id),
#             data=dumps(payload),
#             content_type='application/json'            
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.json()['category'], category_id)
