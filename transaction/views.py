from helpers.helpers import validate_date
from transaction.models import Transaction
from transaction.serializers import TransactionSerializer, TransactionDetailSerializer, TransactionSummarySerializer
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum, Count

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
        print('llega')
        date = self.request.query_params.get('date_month')
        if not date:
            return Response({'400': "date_month it's required."}, status=status.HTTP_400_BAD_REQUEST)
        date = validate_date(date)
        if date is False:
            return Response({'400': 'Invalid date format.'}, status=status.HTTP_400_BAD_REQUEST)
        transactions = self.get_queryset().filter(user=user)
        transactions = Transaction.objects.filter(
            transaction_date__range=[date.start_of('month'), date.end_of('month')]
        ).values('category').order_by('category').annotate(total_spend=Sum('amount'),num_transaction=Count('category'))

        data = TransactionSummarySerializer(transactions, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)