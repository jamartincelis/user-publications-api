from transaction.models import Transaction
from transaction.serializers import TransactionSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response 
from rest_framework.decorators import api_view

@api_view(['GET'])
def transaction_list(request, user):
    if request.method == 'GET':
        budgets = Transaction.objects.filter(user=user)
        serializer = TransactionSerializer(budgets, many=True)
        return Response(serializer.data)    

class TransactionDetail(RetrieveUpdateDestroyAPIView):
    """
    Permite retornar, actualizar o borrar una Transaccion.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer