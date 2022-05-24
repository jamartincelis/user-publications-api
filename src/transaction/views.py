from os import environ

import pendulum

import requests

from django.db.models import Sum, Count, Q, Case, When, F, FloatField, IntegerField

from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from budget.models import Budget

from transaction.models import Transaction
from transaction.serializers import TransactionSerializer, TransactionSummarySerializer
from catalog.helpers import validate_user_accounts


class TransactionsByMonth(ListAPIView):
    """
    Devuelve la lista de transacciones del usuario de un mes en específico
    """

    def get(self, request, user):
        date = validate_date(self.request.query_params.get('date_month'))
        if not date:
            return Response({'400': "Invalid date format."}, status=status.HTTP_400_BAD_REQUEST)
        transactions = Transaction.objects.prefetch_related('transaction_category').filter(
            user=self.kwargs['user_id'],
            transaction_date__range=[date.start_of('month'), date.end_of('month')]
        )
        return Response(data=TransactionSerializer(transactions, many=True).data, status=status.HTTP_200_OK)


class TransactionDetail(RetrieveUpdateAPIView):
    """
    Permite retornar, actualizar o borrar una Transaccion.
    """
    def get(self):
        try:
            transaction = Transaction.objects.prefetch_related('transaction_category').get(
                pk=self.kwargs['pk'],
                user_id=self.kwargs['user_id']
            )
            return Response(TransactionSerializer(transaction).data, status=status.HTTP_200_OK)
        except Transaction.DoesnotExist:
            return Response('Transaction not found', status=status.HTTP_404_NOT_FOUND)



class TransactionsByCategoryAndMonth(ListAPIView):
    """
    Devuelve las transacciones del usuario filtradas por mes y categoría
    """
    serializer_class = TransactionSerializer
    filterset_fields = ['date_month']

    def get_queryset(self):
        return Transaction.objects.filter(
            user_id=self.kwargs['user_id'], 
            category_id=self.kwargs['category_id']
        )

    def get(self, request, user, category):
        date = validate_date(self.request.query_params.get('date_month'))
        if date is False:
            return Response({'400': 'Invalid date format.'}, status=status.HTTP_400_BAD_REQUEST)
        transactions = self.get_queryset().filter(transaction_date__range=[date.start_of('month'), date.end_of('month')])
        data = TransactionSerializer(transactions, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)


class TransactionsCategoriesSummarybyMonth(ListAPIView):
    """
    Devuelve el resumen de transacciones por categorías del mes solicitado
    """
    queryset = Transaction.objects.all()
    filterset_fields = ['date_month']
    serializer_class = TransactionSummarySerializer

    def get(self, request, user):
        date = validate_date(self.request.query_params.get('date_month'))
        if not date:
            return Response({'400': "Invalid date format."}, status=status.HTTP_400_BAD_REQUEST)
        transactions = self.get_queryset().filter(user=user,
            transaction_date__range=[date.start_of('month'), date.end_of('month')]
        ).values('category').order_by('category').annotate(total_spend=Sum('amount'), num_transaction=Count('category'))
        data = TransactionSummarySerializer(transactions, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)


class ExpensesSummary(APIView):
    """
    Devuelve el resumen de egresos y presupuestos por categoría.
    """
    grouped_expenses = {}
    budgets = []
    data = {
        'global_expenses': 0.0,
        'categories': []
    }

    def group_transactions(self, transactions):
        # Se genera un diccionario con la suma del monto y la suma del número de transacciones y se agrupan
        # por categoría
        for transaction in transactions:
            amount = float(transaction['amount'])
            category = str(transaction['category'])
            try:
                self.grouped_expenses[category]['amount'] += amount
                self.grouped_expenses[category]['count'] += 1
                self.grouped_expenses[category]['average'] = 1000 
            except KeyError:
                self.grouped_expenses[category] = {
                    'amount': amount,
                    'count': 1,
                    'average': 1000
                }
            self.data['global_expenses'] += abs(amount)

    def get_expenses(self, category):
        try:
            return self.grouped_expenses[category]
        except KeyError:
            return {
                'amount': 0.0,
                'count': 0
            }

    def get_budget(self, category, amount):
        try:
            budget = self.budgets.get(category=category)
        except Budget.DoesNotExist:
            budget = False
        except Budget.MultipleObjectsReturned:
            budget = False
        return {
            'id': str(budget.id) if budget else None,
            'amount': budget.amount if budget else 0.0,
            'budget_date': str(budget.budget_date) if budget else None,
            'category': str(category) if budget else None,
            'has_budget': True if budget else False,
            'budget_spent': round(abs(amount/float(budget.amount))*100, 2) if budget and amount != 0 else 0.0
        }

    def merge_data(self):
        # se obtiene las categorias de egresos
        categories = expenses_categories['expenses_categories']
        for category in categories:
            expenses = self.get_expenses(category['id'])
            budget = self.get_budget(category['id'], expenses['amount'])
            percentage = expenses['amount'] / self.data['global_expenses'] if self.data['global_expenses'] != 0 else 0.0
            self.data['categories'].append(
                {
                    'category': category,
                    'budget': budget,
                    'expenses': expenses,
                    'percentage': round(abs(percentage)*100, 2),
                    'disabled': True if abs(expenses['amount']) < 1 else False,
                    'amount': expenses['amount']
                }
            )
        self.data['categories'] = sorted(self.data['categories'], key=lambda x:x['amount'])

    def get_other_expenses(self):
        amount = 0.0
        percentage = 0.0
        if len(self.grouped_expenses) > 5:
            for x in self.data['categories'][5:]:
                amount += x['amount']
            percentage = round(amount / self.data['global_expenses'] * 100, 2)
        self.data['other_expenses'] = {
            'amount': amount,
            'percentage': percentage,
            'disabled': True if amount == 0 else False
        }

    def get(self, request, user):
        date = validate_date(self.request.query_params.get('date_month'))
        if not date:
            return Response({'400': "Invalid date format."}, status=status.HTTP_400_BAD_REQUEST)
        self.grouped_expenses = {}
        self.budgets = []
        self.data = {
            'global_expenses': 0.0,
            'categories': []
        }
        transactions = Transaction.objects.filter(
            user=user,
            transaction_date__range=[date.start_of('month'), date.end_of('month')],
            amount__lt=0
        ).values('amount', 'category').order_by('category')
        self.budgets = Budget.objects.filter(
            user=user,
            budget_date__range=[date.start_of('month').strftime('%Y-%m-%d'), date.end_of('month').strftime('%Y-%m-%d')]
        )
        self.group_transactions(transactions)
        self.merge_data()
        self.get_other_expenses()
        return Response(self.data, status=status.HTTP_200_OK)


class MonthlyBalance(APIView):
    """
    Permite retornar el balance mensual del usuario.
    """

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

    def get(self, request, user):
        now = pendulum.now().subtract(years=1)
        start_date = pendulum.datetime(now.year, now.month, 1)
        end_date = pendulum.now().subtract(months=1).end_of('month')
        dates = []
        while start_date < end_date:
            dates.append(start_date)
            start_date = start_date.add(months=1)
        years_dict = {}
        for date in dates:
            data = Transaction.objects.filter(
                transaction_date__range=[date.start_of('month'), date.end_of('month')],
                    user=user,
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
        return Response([v for k, v in years_dict.items()], status=status.HTTP_200_OK)


class MonthlyCategoriesBalance(APIView):
    """
    Permite retornar el balance mensual por categoría del usuario.
    """

    def month_params(self, data, date, budget):
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

    def get(self, request, user, category):
        now = pendulum.now().subtract(years=1)
        start_date = pendulum.datetime(now.year, now.month, 1)
        end_date = pendulum.now().subtract(months=1).end_of('month')
        dates = []
        while start_date < end_date:
            dates.append(start_date)
            start_date = start_date.add(months=1)
        years_dict = {}
        month = 1
        for date in dates:
            try:
                budget = Budget.objects.get(user=user, category=category, 
                    budget_date__month=month)
            except Budget.DoesNotExist:
                budget = None
            data = Transaction.objects.filter(
                transaction_date__range=[date.start_of('month'), date.end_of('month')],
                user=user,
                category=category
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
        return Response([v for k, v in years_dict.items()], status=status.HTTP_200_OK)


class NewTransaction(APIView):
    """
    Permite crear una transacción a aprtir de un número de cuenta
    """

    def post(self, request):
        data = request.data
        account = validate_user_accounts(data['account_number'])
        if account is not False:
            try:
                transaction = Transaction.objects.create(
                    account=account['id'],
                    user_id=account['user_'],
                    amount=data['amount'],
                    description=data['description'],
                    transaction_date=data['transaction_date']
                )
                return Response(TransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)
            except KeyError:
                return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)
        return Response('Account not found', status=status.HTTP_404_NOT_FOUND)
