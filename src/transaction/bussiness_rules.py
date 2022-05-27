from os import environ

import requests

import pendulum

from django.db.models import Sum, Count, Q, Case, When, F, FloatField, IntegerField

from helpers.helpers import months_dict

from catalog.models import Item
from catalog.serializers import ItemSerializer

from budget.models import Budget

from transaction.models import Transaction


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


class BuildMonthlyBalanceResponse:

    def __init__(self, user_id):
        self.user_id = user_id


    def month_params(self, data, date):
        incomes = 0.0 if data['incomes'] is None else data['incomes']
        expenses = 0.0 if data['expenses'] is None else data['expenses']
        return {
            'year': date.year,
            'month': months_dict[date.month],
            'incomes': incomes,
            'expenses': expenses,
            'balance': incomes + expenses,
            'disabled': True if (data['incomes'] or data['expenses']) is None else False
        }

    def get_data(self):
        start_date = pendulum.now().subtract(months=int(environ.get('MAX_MONTHS'))-1)
        end_date = pendulum.now().end_of('month')
        dates = []
        while start_date < end_date:
            dates.append(start_date)
            start_date = start_date.add(months=1)

        years_dict = {}
        for date in dates:
            data = Transaction.objects.filter(
                transaction_date__range=[date.start_of('month'), date.end_of('month')],
                    user_id=self.user_id,
                ).aggregate(
                incomes=Sum(Case(
                    When(amount__gt=0, then=F('amount')),
                    output_field=FloatField(),
                )),
                expenses=Sum(Case(
                    When(amount__lt=0, then=F('amount')),
                    output_field=FloatField(),
                )),
            )
            try:
                years_dict[date.year]['months'].append(self.month_params(data, date))
            except KeyError:
                years_dict[date.year] = {
                    'year': date.year,
                    'months': [
                        self.month_params(data, date)
                    ]
                }
        return [v for k, v in years_dict.items()]


class BuildMonthlyBalanceByCategoryResponse:

    def __init__(self, user_id, category):
        self.user_id = user_id
        self.category = category

    def month_params(self, data, date, budget):
        # Requiere refactor
        expenses_sum = 0.0 if data['expenses_sum'] is None else abs(data['expenses_sum'])
        expenses_count = 0 if data['expenses_count'] is None else abs(data['expenses_count'])
        budget_spent = (abs(expenses_sum)*100)/float(budget.amount) if budget else 0
        return {
            'year': date.year,
            'month': months_dict[date.month],
            'expenses_sum': expenses_sum,
            'expenses_count': expenses_count,
            'average': 0.0 if expenses_count == 0 else float(expenses_sum/expenses_count),
            'budget': budget.amount if budget else 0,
            'budget_spent': round(budget_spent,2),
            'has_budget': True if budget else False,
            'budget_id': budget.id if budget else False,
            'disabled': True if expenses_count == 0 else False
        }

    def get_data(self):
        start_date = pendulum.now().subtract(months=int(environ.get('MAX_MONTHS'))-1)
        end_date = pendulum.now().end_of('month')
        dates = []
        while start_date < end_date:
            dates.append(start_date)
            start_date = start_date.add(months=1)
        years_dict = {}
        month = 1
        for date in dates:
            try:
                budget = Budget.objects.get(
                    user_id=self.user_id,
                    category=self.category, 
                    budget_date__month=month
                )
            except Budget.DoesNotExist:
                budget = None
            data = Transaction.objects.filter(
                transaction_date__range=[date.start_of('month'), date.end_of('month')],
                user_id=self.user_id,
                category=self.category
                ).aggregate(
                expenses_sum=Sum(Case(
                    When(amount__lt=0, then=F('amount')),
                    output_field=FloatField(),
                )),
                expenses_count=Count(Case(
                    When(amount__lt=0, then=1),
                    output_field=IntegerField(),
                ))
            )
            try:
                years_dict[date.year]['months'].append(self.month_params(data, date, budget))
            except KeyError:
                years_dict[date.year] = {
                    'year': date.year,
                    'months': [
                        self.month_params(data, date, budget)
                    ]
                }
            month+=1
            if month > 12:
               month = 1 
        return [v for k, v in years_dict.items()]
