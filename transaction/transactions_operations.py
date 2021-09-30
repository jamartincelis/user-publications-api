from transaction.models import Transaction
from catalog.models import Code
import pandas as pd
from budget.models import Budget
import numpy as np
from operator import itemgetter


class TransactionsOperations():
    def __init__(self, *args, **kwargs):
        pass

    def _get_budget_percent(self, budget, amount):

        if budget == 0:
            return 0
        return np.round(float( (budget + amount)*100 / budget))


    def get_expense_summary(self, user, start_date, end_date):
        '''[summary]

        Parameters
        ----------
        user : [type]
            [description]
        start_date : [type]
            [description]
        end_date : [type]
            [description]

        Returns
        -------
        [type]
            [description]
        '''

        # Get data to process
        transactions_query_dict = Transaction.objects.filter(
            user=user,
            transaction_date__range=(start_date, end_date)).values()
        categories_dict = Code.objects.filter(
            code_type="1ec6a6b5-65d5-4a8c-85d0-4364c141aefd").values()

        user_budgets_dict = Budget.objects.filter(
            user=user).values()
        user_budgets = pd.DataFrame.from_dict(
            user_budgets_dict)
        transactions = pd.DataFrame.from_dict(
            transactions_query_dict)
        del user_budgets["id"]
        del user_budgets["user_id"]
        user_budgets['budget'] = user_budgets['amount']
        del user_budgets['amount']

        # Process stats for transactions
        transactions_negative = transactions[
            transactions['amount'] < 0].copy()
        global_expenses = transactions_negative['amount'].sum()
        transactions_negative_stats = transactions_negative.groupby([
            'category_id']).agg(
                {'category_id':'first',
                    'id': 'count',
                    'amount': 'sum'
                    })

        transactions_negative_stats['percentage'] = transactions_negative_stats['amount'].apply(
            lambda x: (np.round(float(100 * x / global_expenses),2)))

        # Merege and process budgets with transactions
        transactions_negative_stats.index = ['category_id_index', 'two']

        transactions_negative_stats = transactions_negative_stats.merge(
            user_budgets, on='category_id', how='left')

        transactions_negative_stats['budget'] = transactions_negative_stats['budget'].fillna(0)
        transactions_negative_stats['budget_spent'] = transactions_negative_stats.apply(
            lambda x: self._get_budget_percent(x['budget'], x['amount']), axis=1)


        # Adapt the object to return
        transactions_negative_stats_dict = transactions_negative_stats.to_dict('records')

        categories_expends_stats = []

        for categorie_dict in categories_dict:
            for transactions_negative_stat in transactions_negative_stats_dict:
                if transactions_negative_stat['category_id'] == categorie_dict['id']:
                    adapted_category = {
                        "category": categorie_dict,
                        "expenses_count": transactions_negative_stat['id'],
                        "spend": transactions_negative_stat['amount'],
                        "percentage": transactions_negative_stat['percentage'],
                        "budget": transactions_negative_stat['budget'],
                        "budget_spent": transactions_negative_stat['budget_spent'],
                        "has_budget": True,
                        "disabled": True
                    }
                else:
                    adapted_category = {
                        "category": categorie_dict,
                        "expenses_count": 0,
                        "spend":0,
                        "percentage": 0,
                        "budget": 0,
                        "budget_spent": 0,
                        "has_budget": False,
                        "disabled": False
                    }

                categories_expends_stats.append(adapted_category)

        sorted_categories_expends_stats = sorted(
            categories_expends_stats, reverse=True, key=itemgetter('expenses_count'))

        return {
            "global_expenses": global_expenses,
            "expenses": sorted_categories_expends_stats
        }
