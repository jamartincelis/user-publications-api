import pendulum

from django.db.models import Sum, Count, Q, Case, When, F, FloatField, IntegerField
from django.db import connection

from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from helpers.helpers import validate_date, months_dict

from catalog.models import Code
from catalog.serializers import CodeSerializer

from budget.models import Budget

from transaction.models import Transaction
from transaction.serializers import MonthlyBalanceSerializer, TransactionSerializer, TransactionDetailSerializer,\
    TransactionSummarySerializer


class TransactionList(ListAPIView):
    """
    Devuelve la lista de transacciones del usuario
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filterset_fields = ['date_month']

    def get(self, request, user):
        date = validate_date(self.request.query_params.get('date_month'))
        if not date:
            return Response({'400': "Invalid date format."}, status=status.HTTP_400_BAD_REQUEST)
        transactions = self.get_queryset().prefetch_related('category').filter(account__user=user)
        transactions = transactions.filter(transaction_date__range=[date.start_of('month'), date.end_of('month')])
        data = TransactionSerializer(transactions, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)


class TransactionDetail(RetrieveUpdateAPIView):
    """
    Permite retornar, actualizar o borrar una Transaccion.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class Category(ListAPIView):
    """
    Devuelve las transacciones del usuario filtradas por mes y categoría
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filterset_fields = ['date_month']

    def get(self, request, user, category):
        date = validate_date(self.request.query_params.get('date_month'))
        if date is False:
            return Response({'400': 'Invalid date format.'}, status=status.HTTP_400_BAD_REQUEST)
        transactions = self.get_queryset().filter(account__user=user, category=category)
        transactions = transactions.filter(transaction_date__range=[date.start_of('month'), date.end_of('month')])
        data = TransactionSerializer(transactions, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)


# HACIA ABAJO


class CategorySummary(ListAPIView):
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
        ).values('category').order_by('category').annotate(total_spend=Sum('amount'),num_transaction=Count('category'))
        data = TransactionSummarySerializer(transactions, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)


class ExpenseSummaryView(APIView):
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
        for transaction in transactions:
            amount = float(transaction['amount'])
            category = transaction['category']
            try:
                self.grouped_expenses[category]['amount'] += amount
                self.grouped_expenses[category]['count'] += 1
            except KeyError:
                self.grouped_expenses[category] = {
                    'amount': amount,
                    'count': 1
                }
            self.data['global_expenses'] += amount

    def get_expenses(self, category):
        try:
            return self.grouped_expenses[category]
        except KeyError:
            return {
                'amount': 0.0,
                'count': 0
            }

    def get_budget(self, category):
        try:
            budget = self.budgets.get(category=category)
        except Budget.DoesNotExist:
            budget = False
        return {
            'id': str(budget.id) if budget else None,
            'amount': budget.amount if budget else 0.0,
            'budget_date': str(budget.budget_date) if budget else None,
            'category': str(category) if budget else None,
            'has_budget': True if budget else False,
        }

    def merge_data(self):
        categories = Code.objects.filter(code_type__name='transaction_category')
        for category in categories:
            budget = self.get_budget(category.id)
            expenses = self.get_expenses(category.id)
            percentage = expenses['amount'] / float(budget['amount']) if budget['has_budget'] is True else 0
            self.data['categories'].append(
                {
                    'category': CodeSerializer(category).data,
                    'budget': budget,
                    'expenses': expenses,
                    'percentage': '{}%'.format(int(abs(percentage)*100)),
                    'disabled': True if abs(expenses['amount']) < 1 else False,
                    'amount': expenses['amount']
                }
            )
        self.data['categories'] = sorted(self.data['categories'], key=lambda x:x['amount'])

    def get(self, request, user):
        date = validate_date(self.request.query_params.get('date_month'))
        if not date:
            return Response({'400': "Invalid date format."}, status=status.HTTP_400_BAD_REQUEST)
        transactions = Transaction.objects.filter(
            account__user=user,
            transaction_date__range=[date.start_of('month'), date.end_of('month')],
            amount__lt=0
        ).values('amount', 'category')
        self.budgets = Budget.objects.filter(
            user=user, budget_date__range=[date.start_of('month'), date.end_of('month')])
        self.group_transactions(transactions)
        self.merge_data()
        return Response(self.data, status=status.HTTP_200_OK)


class MonthlyBalanceView(APIView):
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
        year = Transaction.objects.filter(account__user=user).order_by('transaction_date').first().transaction_date.year
        start_date = pendulum.datetime(year, 1, 1)
        end_date = pendulum.now().end_of('year')
        dates = []
        while start_date.year <= end_date.year:
            dates.append(start_date)
            start_date = start_date.add(months=1)
        years_dict = {}
        for date in dates:
            data = Transaction.objects.filter(
                transaction_date__range=[date.start_of('month'), date.end_of('month')],
                account__user=user,
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


class MonthlyCategoryBalanceView(APIView):
    """
    Permite retornar el balance mensual por categoría del usuario.
    """

    def month_params(self, data, date):
        expenses_sum = 0.0 if data['expenses_sum'] is None else data['expenses_sum']
        expenses_count = 0 if data['expenses_count'] is None else data['expenses_count']
        return {
            'year': date.year,
            'month': months_dict[date.month],
            'expenses_sum': expenses_sum,
            'expenses_count': expenses_count,
            'average': 0.0 if expenses_count == 0 else float(expenses_sum/expenses_count),
            'budget': float(date.month * 1000),
            'budget_spent': '{}%'.format(date.month),
            'has_budget': True,
            'disabled': True if data['expenses_count'] == 0 else False
        }

    def get(self, request, user, category):
        year = Transaction.objects.filter(
            user=user, category=category).order_by('transaction_date').first().transaction_date.year
        start_date = pendulum.datetime(year, 1, 1)
        end_date = pendulum.now().end_of('year')
        dates = []
        while start_date.year <= end_date.year:
            dates.append(start_date)
            start_date = start_date.add(months=1)
        years_dict = {}
        for date in dates:
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
                years_dict[date.year]['months'].append(self.month_params(data, date))
            except KeyError:
                years_dict[date.year] = {
                    'year': date.year,
                    'months': [
                        self.month_params(data, date)
                    ]
                }
        return Response([v for k, v in years_dict.items()], status=status.HTTP_200_OK)
