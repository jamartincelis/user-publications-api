# from json import dumps
# from django.test import TestCase, Client
# from budget.models import Budget
# from rest_framework import status

# class BudgetTestCase(TestCase):

#     client = Client()
#     fixtures = [
#         'user/fixtures/users.yaml',
#         'catalog/fixtures/codetype.yaml',
#         'catalog/fixtures/transactions_categories.yaml',
#         'budget/fixtures/budgets.yaml'
#     ]
#     DATE_MONTH = "?date_month={}"
#     URL_BASE = '/user/{}/budgets/'
#     URL_DETAIL = URL_BASE + '{}/'
#     URL_DATE_MONTH = URL_BASE + DATE_MONTH

#     def test_budgets_list(self):
#         user_id = '0390a508-dba5-4344-b77f-93e1227d42f4'
#         budgets = Budget.objects.filter(user=user_id,
#             budget_date__range=['2021-09-01', '2021-09-30']
#         )
#         date_month = "2021-09"
#         response = self.client.get(self.URL_DATE_MONTH.format(user_id,date_month))
#         data = response.json()
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(budgets.count(), len(data))

#     def test_budget_detail(self):
#         user_id = '479ec168013945d0b7042bc4e5d0c4fb'
#         budget_id = '45a80dbbea714ce390b36761bcbf365c'
#         budget = Budget.objects.get(user=user_id,id=budget_id)
#         response = self.client.get(self.URL_DETAIL.format(user_id,budget_id))
#         data = response.json()
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(data['id'], str(budget.id))
#         self.assertEqual(data['user'], str(budget.user.id))
#         self.assertEqual(data['category'], str(budget.category.id))

#     def test_add_budget(self):
#         user_id = '0390a508-dba5-4344-b77f-93e1227d42f4'
#         payload = {
#             "amount": 3000,
#             "budget_date": "2021-09-09T15:20:30-04:00",
#             "user": "479ec168-0139-45d0-b704-2bc4e5d0c4fb",
#             "category": "22118f55-e6a9-46b0-ae8f-a063dda396e0"
#         }
#         response = self.client.post(
#             self.URL_BASE.format(user_id),
#             data=dumps(payload),
#             content_type='application/json'            
#         )
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)