from django.test import TestCase, Client
from transaction.models import Transaction

class BudgetTestCase(TestCase):

    client = Client()
    fixtures = [
        'user/fixtures/users.yaml',
        'catalog/fixtures/codetype.yaml',
        'catalog/fixtures/transactions_categories.yaml',
        'transaction/fixtures/transactions.yaml'
    ]

    def test_transactions_of_user(self):
        user_id = '0390a508-dba5-4344-b77f-93e1227d42f4'
        transactions = Transaction.objects.filter(user=user_id)
        response = self.client.get('/user/{}/transactions/'.format(user_id))
        data = response.json()
        self.assertEqual(transactions.count(), len(data))

    def test_specific_transaction_of_user(self):
        user_id = '479ec168013945d0b7042bc4e5d0c4fb'
        transaction_id = '68e18783-8b51-4618-af83-50c77f25871d'
        transaction = Transaction.objects.get(user=user_id,id=transaction_id)
        response = self.client.get('/user/{}/transactions/{}/'.format(user_id,transaction_id))
        data = response.json()
        self.assertEqual(data['id'], str(transaction.id))
        self.assertEqual(data['user'], str(transaction.user.id))
        self.assertEqual(data['category']['id'], str(transaction.category.id))