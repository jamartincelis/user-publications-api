from os import environ

import requests

from catalog.models import Item
from catalog.serializers import ItemSerializer


def validate_user_accounts(data):
    try:
        core_url = environ.get('CORE_SERVICE_URL')
        response = requests.get(self.core_url+'accounts/?number={}'.format(account_number), timeout=1)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException:
        return False
    return False


class BuildExpensesSummaryByMonthResponse:

    def __init__(self, transactions, budgets):
        self.grouped_transactions = {}
        self.grouped_budgets = []
        self.transactions = transactions
        self.budgets = budgets
        self.data = {
            'global_expenses': 0.0,
            'categories': []
        }
        items = Item.objects.filter(catalog__catalog_name='expenses_categories')
        self.expenses_categories =  {
            str(item.id): ItemSerializer(item).data
            for item in items
        }

    def get_expenses(self, category):
        try:
            return self.grouped_transactions[category]
        except KeyError:
            return {
                'amount': 0.0,
                'count': 0
            }

    def get_budget(self, category, amount):
        try:
            budget = self.budgets.get(category=category)
            return {
                'id': str(budget.id),
                'amount': budget.amount,
                'budget_date': str(budget.budget_date),
                'category': str(category),
                'has_budget': True,
                'budget_spent': round(abs(amount/float(budget.amount))*100, 2)
            }
        except Exception as e:
            return {
                'id':None,
                'amount': 0.0,
                'budget_date': None,
                'category': None,
                'has_budget': False,
                'budget_spent': 0.0
            }
    def group_transactions(self):
        for transaction in self.transactions:
            amount = float(transaction['amount'])
            category = str(transaction['category'])
            try:
                self.grouped_transactions[category]['amount'] += amount
                self.grouped_transactions[category]['count'] += 1
            except KeyError:
                self.grouped_transactions[category] = {
                    'amount': amount,
                    'count': 1
                }
            self.data['global_expenses'] += abs(amount)

    def merge_data(self):
        for category in self.expenses_categories:
            expenses = self.get_expenses(category)
            budget = self.get_budget(category, expenses['amount'])
            percentage = expenses['amount'] / self.data['global_expenses'] if self.data['global_expenses'] != 0 else 0.0
            self.data['categories'].append(
                {
                    'category': self.expenses_categories[category],
                    'budget': budget,
                    'expenses': expenses,
                    'percentage': round(abs(percentage)*100, 2),
                    'disabled': True if abs(expenses['amount']) < 1 else False,
                    'amount': expenses['amount']
                }
            )

    def other_expenses(self):
            self.data['categories'] = sorted(self.data['categories'], key=lambda x:x['amount'])
            amount = 0.0
            percentage = 0.0
            if len(self.grouped_transactions) > 5:
                for x in self.data['categories'][5:]:
                    amount += x['amount']
                percentage = round(amount / data['global_expenses'] * 100, 2)
            self.data['other_expenses'] = {
                'amount': amount,
                'percentage': percentage,
                'disabled': True if amount == 0 else False
            }

    def get_data(self):
        self.group_transactions()
        self.merge_data()
        self.other_expenses()
        return self.data
