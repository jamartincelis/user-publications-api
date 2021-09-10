from transaction.models import Transaction
from transaction.serializers import TransactionSerializer
from rest_framework import generics
from rest_framework.decorators import authentication_classes, permission_classes
 
@authentication_classes([])
@permission_classes([])
class TransactionList(generics.ListCreateAPIView):
    """
    Permite listar y crear transacciones.
    """
    serializer_class = TransactionSerializer
        
    def get_queryset(self):
        """
        Se realizan los filtros de acuerdo a los parámetros ingresados
        """        
        queryset = Transaction.objects.all()
        return queryset
    
    
class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Permite retornar, actualizar o borrar una Transaccion.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer