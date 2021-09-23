import pendulum

from django.db.models import Sum, Count, Q, Case, When, F, FloatField, IntegerField
from django.db import connection

from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from query_raw.queries import ANIOS_TRANSACCIONES, BALANCE_MENSUAL, EGRESOS_PRESUPUESTOS

from helpers.helpers import validate_date, months_dict

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
        transactions = self.get_queryset().filter(user=user)            
        date = self.request.query_params.get('date_month')
        if not date:
            return Response({'400': "date_month it's required."}, status=status.HTTP_400_BAD_REQUEST)
        date = validate_date(date)
        if date is False:
            return Response({'400': 'Invalid date format.'}, status=status.HTTP_400_BAD_REQUEST)  
        transactions = transactions.filter(transaction_date__range=[date.start_of('month'), date.end_of('month')])
        data = TransactionSerializer(transactions, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)


class TransactionDetail(RetrieveUpdateAPIView):
    """
    Permite retornar, actualizar o borrar una Transaccion.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionDetailSerializer


class Category(ListAPIView):
    """
    Devuelve las transacciones del usuario filtradas por mes y categoría
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filterset_fields = ['date_month']

    def get(self, request, user, category):
        transactions = self.get_queryset().filter(user=user,category=category)
        date = self.request.query_params.get('date_month')
        if not date:
            return Response({'400': "date_month it's required."}, status=status.HTTP_400_BAD_REQUEST)
        date = validate_date(date)
        if date is False:
            return Response({'400': 'Invalid date format.'}, status=status.HTTP_400_BAD_REQUEST)
        transactions = transactions.filter(transaction_date__range=[date.start_of('month'), date.end_of('month')])
        data = TransactionSerializer(transactions, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)


class CategorySummary(ListAPIView):
    """
    Devuelve el resumen de transacciones por categorías del mes solicitado
    """
    queryset = Transaction.objects.all()
    filterset_fields = ['date_month']
    serializer_class = TransactionSummarySerializer
    
    def get(self, request, user):
        date = self.request.query_params.get('date_month')
        if not date:
            return Response({'400': "date_month it's required."}, status=status.HTTP_400_BAD_REQUEST)
        date = validate_date(date)
        if date is False:
            return Response({'400': 'Invalid date format.'}, status=status.HTTP_400_BAD_REQUEST)
        transactions = self.get_queryset().filter(user=user,
            transaction_date__range=[date.start_of('month'), date.end_of('month')]
        ).values('category').order_by('category').annotate(total_spend=Sum('amount'),num_transaction=Count('category'))
        data = TransactionSummarySerializer(transactions, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)


class ExpenseSummaryView(APIView):
    """
    Devuelve el resumen de egresos y presupuestos por categoría.
    """
    def get(self, request, user):
        date = self.request.query_params.get('date_month')
        if not date:
            return Response({'400': "date_month it's required."}, status=status.HTTP_400_BAD_REQUEST)
        date = validate_date(date)
        if date is False:
            return Response({'400': 'Invalid date format.'}, status=status.HTTP_400_BAD_REQUEST)
        start = date.start_of('month')
        end = date.end_of('month')
        with connection.cursor() as cursor:
            cursor.execute(EGRESOS_PRESUPUESTOS, [start, end, user,user, start, end])
            columns = [desc[0] for desc in cursor.description]
            datos = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ] 
        return Response(datos, status=status.HTTP_200_OK)


class MonthlyBalanceView(APIView):
    """
    Permite retornar el balance mensual del usuario.
    """
    def get(self, request, user):
        year = Transaction.objects.filter(user=user).order_by('transaction_date').first().transaction_date.year
        start_date = pendulum.datetime(year, 1, 1)
        end_date = pendulum.now().end_of('year')
        dates = []
        data_array = []
        while start_date.year <= end_date.year:
            dates.append(start_date)
            start_date = start_date.add(months=1)
        for date in dates:
            data = Transaction.objects.filter(
                transaction_date__range=[date.start_of('month'), date.end_of('month')],
                user_id=user,
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
            incomes = 0.0 if data['incomes'] is None else data['incomes']
            expenses = 0.0 if data['expenses'] is None else data['expenses']
            data_array.append(
                {
                    'year': date.year,
                    'month': months_dict[date.month],
                    'incomes': incomes,
                    'expenses': expenses,
                    'balance': incomes + expenses,
                    'disabled': True if (data['incomes'] and data['expenses']) is None else False
                }
            )
        return Response(data_array, status=status.HTTP_200_OK)
