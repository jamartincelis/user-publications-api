from transaction.models import Transaction
from catalog.models import Code
import pandas as pd
from budget.models import Budget
import numpy as np
from operator import itemgetter
import uuid

class TransactionsOperations():
    def __init__(self, *args, **kwargs):
        pass

    def _get_budget_percent(self, budget, amount):

        if budget == 0:
            return 0
        return np.round(float( (budget + amount)*100 / budget))



    def get_expense_summary(self, user: str, start_date:str, end_date: str, show_rows=6):
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
        user_budgets['category_id_new'] = user_budgets['category_id']
        del user_budgets['category_id']
        del user_budgets['amount']
        del user_budgets['budget_date']

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
        transactions_negative_stats['category_id_new'] = transactions_negative_stats['category_id']
        del transactions_negative_stats['category_id']

        transactions_negative_stats = transactions_negative_stats.merge(
            user_budgets, on='category_id_new', how='left')

        transactions_negative_stats['budget'] = transactions_negative_stats['budget'].fillna(0)
        transactions_negative_stats['budget_spent'] = transactions_negative_stats.apply(
            lambda x: self._get_budget_percent(x['budget'], x['amount']), axis=1)

        transactions_negative_stats = transactions_negative_stats.sort_values(
            by=['id'], ascending=False, ignore_index=True)

        row_lenght = len(transactions_negative_stats)
        compact_negative_stats_dict = {}
        show_rows = show_rows - 1

        if row_lenght >= show_rows:
            compact_transactions_negative_stats = transactions_negative_stats[show_rows:]
            transactions_negative_stats = transactions_negative_stats[0:show_rows]
            print(compact_transactions_negative_stats)

            compact_negative_stats_dict = {
                "id": compact_transactions_negative_stats["id"].sum(),
                "amount": compact_transactions_negative_stats["amount"].sum(),
                "budget": compact_transactions_negative_stats["budget"].sum(),
                "percentage": compact_transactions_negative_stats["percentage"].sum(),
                "category_id_new": "38e570af-1241-426c-afa5-f874b1c49128"
            }

            compact_negative_stats_dict["budget_spent"] = self._get_budget_percent(
                compact_negative_stats_dict['budget'], compact_negative_stats_dict['budget'])

        # Adapt the object to return
        transactions_negative_stats_dict = transactions_negative_stats.to_dict('records')
        if compact_negative_stats_dict:
            transactions_negative_stats_dict.append(
                compact_negative_stats_dict)

            categories_expends_stats = []

        for transactions_negative_stat in transactions_negative_stats_dict:
            for categorie_dict in categories_dict:

                if str(transactions_negative_stat['category_id_new']) == str(categorie_dict['id']):
                    adapted_category = {
                        "category": categorie_dict,
                        "expenses_count": transactions_negative_stat['id'],
                        "spend": transactions_negative_stat['amount'],
                        "percentage": transactions_negative_stat['percentage'],
                        "budget": transactions_negative_stat['budget'],
                        "budget_spent": transactions_negative_stat['budget_spent'],
                        "has_budget": True if transactions_negative_stat['budget'] > 0 else False,
                        "disabled": False if transactions_negative_stat['budget'] > 0 else False
                    }
                # else:
                #     adapted_category = {
                #         "category": categorie_dict,
                #         "expenses_count": 0,
                #         "spend":0,
                #         "percentage": 0,
                #         "budget": 0,
                #         "budget_spent": 0,
                #         "has_budget": False,
                #         "disabled": False
                #     }

                    categories_expends_stats.append(adapted_category)


        return {
            "global_expenses": global_expenses,
            "expenses": categories_expends_stats
        }
