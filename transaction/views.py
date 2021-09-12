from transaction.models import Transaction
from transaction.serializers import TransactionSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status

class TransactionList(ListAPIView):
    """
    Devuelve la lista de transacciones del usuario
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filterset_fields = ['date_month']

    def get(self, request, user):
        transactions = self.get_queryset().filter(user=user)            
        data = TransactionSerializer(transactions, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)

class TransactionDetail(RetrieveUpdateDestroyAPIView):
    """
    Permite retornar, actualizar o borrar una Transaccion.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer