from django.test import TestCase, Client
from budget.models import Budget

class BudgetTestCase(TestCase):

    client = Client()
    fixtures = [
        'user/fixtures/users.yaml',
        'catalog/fixtures/codetype.yaml',
        'catalog/fixtures/transactions_categories.yaml',
        'budget/fixtures/budgets.yaml'
    ]

    def test_budgets_of_user(self):
        user_id = '0390a508-dba5-4344-b77f-93e1227d42f4'
        budgets = Budget.objects.filter(user=user_id)
        response = self.client.get('/user/{}/budgets/'.format(user_id))
        data = response.json()
        self.assertEqual(budgets.count(), len(data))

    def test_specific_budget_of_user(self):
        user_id = '479ec168013945d0b7042bc4e5d0c4fb'
        budget_id = '45a80dbbea714ce390b36761bcbf365c'
        budget = Budget.objects.get(user=user_id,id=budget_id)
        response = self.client.get('/user/{}/budgets/{}/'.format(user_id,budget_id))
        data = response.json()
        self.assertEqual(data['id'], str(budget.id))
        self.assertEqual(data['user'], str(budget.user.id))
        self.assertEqual(data['category']['id'], str(budget.category.id))