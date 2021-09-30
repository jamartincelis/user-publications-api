from os import lseek
import transaction
from transaction.models import Transaction
import pandas as pd


class TransactionsOperations():
    def __init__(self, *args, **kwargs):
        pass

    def get_expense_summary(self, user, start_date, end_date):
        transactions_query_dict = Transaction.objects.filter(
            user=user,
            transaction_date__range=(start_date, end_date)).values()

        transactions = pd.DataFrame.from_dict(
            transactions_query_dict)
        print(transactions.describe())

        transactions_negative = transactions[
            transactions['amount'] < 0].copy()

        transactions_negative_stats = transactions_negative.groupby([
            'category_id']).agg(
                {   'id': 'count',
                    'user_id': 'first',
                    'amount': 'sum'
                    })
        # transactions.groupby(
        #     ['category_id']).filter(lambda x: (x['amount'] > 0).any()).agg()

        print(transactions_negative_stats['amount'])
