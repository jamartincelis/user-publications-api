from os import lseek
import transaction
from transaction.models import Transaction
from catalog.models import CodeType, Code
import pandas as pd
from budget.models import Budget
import numpy as np

class TransactionsOperations():
    def __init__(self, *args, **kwargs):
        pass

    def get_expense_summary(self, user, start_date, end_date):
        transactions_query_dict = Transaction.objects.filter(
            user=user,
            transaction_date__range=(start_date, end_date)).values()
        categoires_dict = Code.objects.filter(
            code_type="1ec6a6b5-65d5-4a8c-85d0-4364c141aefd").values()

        user_budgets_dict = Budget.objects.filter(user=user).values()
        user_budgets = pd.DataFrame.from_dict(
            user_budgets_dict)
        transactions = pd.DataFrame.from_dict(
            transactions_query_dict)

        transactions_negative = transactions[
            transactions['amount'] < 0].copy()
        global_expenses = transactions_negative['amount'].sum()
        transactions_negative_stats = transactions_negative.groupby([
            'category_id']).agg(
                {   'id': 'count',
                    'user_id': 'first',
                    'amount': 'sum'
                    })

        transactions_negative_stats['%'] = transactions_negative_stats['amount'].apply(
            lambda x: (100 * x / global_expenses))
        print()
        transactions_negative_stats['%'] = transactions_negative_stats['%'].set_option(
            'precision', 2)
        '''{
			        "category": ok,
			        "spend": 0.0,
				    "percentage": 49.25
			        "budget": 1000.0,
				      "expenses_count": 0,
			        "budget_spent": "1%",
			        "has_budget": true,
					"disabled": true


			    }
        '''
        print(transactions_negative_stats)
