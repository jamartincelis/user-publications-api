import pendulum

from django.db.models import Sum, Count, Q, Case, When, F, FloatField, IntegerField

from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from helpers.helpers import validate_date

from catalog.models import Item
from catalog.serializers import ItemSerializer

from budget.models import Budget

from transaction.models import Transaction
from transaction.serializers import TransactionSerializer
from transaction.bussiness_rules import BuildExpensesSummaryByMonthResponse, BuildMonthlyBalanceResponse,\
    BuildMonthlyBalanceByCategoryResponse


class TransactionsByMonth(ListAPIView):
    """
    Devuelve la lista de transacciones del usuario de un mes en específico
    """

    def get(self, request, user_id):
        date = validate_date(self.request.query_params.get('date_month'))
        if not date:
            return Response({'400': "Invalid date format."}, status=status.HTTP_400_BAD_REQUEST)
        transactions = Transaction.objects.select_related('category', 'account_type').filter(
            user_id=user_id,
            transaction_date__range=[date.start_of('month'), date.end_of('month')]
        )
        return Response(data=TransactionSerializer(transactions, many=True).data, status=status.HTTP_200_OK)


class ExpensesSummarybyMonth(APIView):
    """
    Devuelve el resumen de egresos y presupuestos por categoría de un mes específico
    """

    def get(self, request, user_id):
        date = validate_date(self.request.query_params.get('date_month'))
        if not date:
            return Response({'400': "Invalid date format."}, status=status.HTTP_400_BAD_REQUEST)
        transactions = Transaction.objects.filter(
            user_id=user_id,
            transaction_date__range=[date.start_of('month'), date.end_of('month')],
            amount__lt=0
        ).values('amount', 'category').order_by('category')
        budgets = Budget.objects.filter(
            user_id=user_id,
            budget_date__range=[date.start_of('month'), date.end_of('month')]
        )
        response = BuildExpensesSummaryByMonthResponse(transactions, budgets)
        data = response.get_data()
        return Response(data, status=status.HTTP_200_OK)


class TransactionDetail(RetrieveUpdateAPIView):
    """
    Permite retornar, actualizar o borrar una Transaccion.
    """

    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.select_related('category', 'account_type').all()


class TransactionsByCategoryAndMonth(APIView):
    """
    Devuelve las transacciones del usuario filtradas por mes y categoría
    """

    def get(self, request, user_id, category):
        date = validate_date(self.request.query_params.get('date_month'))
        if date is False:
            return Response({'400': 'Invalid date format.'}, status=status.HTTP_400_BAD_REQUEST)
        summary = Transaction.objects().filter(
            transaction_date__range=[date.start_of('month'), date.end_of('month')]
        )
        data = TransactionSerializer(transactions, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)


class TransactionsCategoriesSummarybyMonth(APIView):
    """
    Devuelve el resumen de transacciones por categorías del mes solicitado
    """

    def get(self, request, user_id):
        date = validate_date(self.request.query_params.get('date_month'))
        if not date:
            return Response({'400': "Invalid date format."}, status=status.HTTP_400_BAD_REQUEST)
        summaries = Transaction.objects.filter(
            user_id=user_id,
            transaction_date__range=[date.start_of('month'), date.end_of('month')]
        ).values('category').order_by('category').annotate(total_spend=Sum('amount'), num_transaction=Count('category'))
        # esto requiere refactor
        for summary in summaries:
            summary['category'] = ItemSerializer(Item.objects.get(id=summary['category'])).data
        return Response(data=summaries, status=status.HTTP_200_OK)


class MonthlyBalance(APIView):
    """
    Permite retornar el balance mensual del usuario.
    """

    def get(self, request, user_id):
        response = BuildMonthlyBalanceResponse(user_id)
        return Response(response.get_data(), status=status.HTTP_200_OK)


class MonthlyBalanceByCategory(APIView):
    """
    Permite retornar el balance mensual por categoría del usuario.
    """

    def get(self, request, user_id, category):
        response = BuildMonthlyBalanceByCategoryResponse(user_id, category)
        return Response(response.get_data(), status=status.HTTP_200_OK)


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
                    transaction_date=data['transaction_date'],
                    category='f37b6770-7fc5-43e0-a837-50926e1ee459' # Sin categoría
                )
                return Response(TransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)
            except KeyError:
                return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)
        return Response('Account not found', status=status.HTTP_404_NOT_FOUND)
