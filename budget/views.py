from budget.serializers import BudgetSerializer
from budget.models import Budget
from rest_framework import generics
from rest_framework.decorators import authentication_classes, permission_classes
 
@authentication_classes([])
@permission_classes([])
class BudgetList(generics.ListCreateAPIView):
    """
    Permite listar y crear presupuestos
    """
    serializer_class = BudgetSerializer
        
    def get_queryset(self):
        """
        Se realizan los filtros de acuerdo a los parámetros ingresados
        """        
        queryset = Budget.objects.all()
        return queryset
    
    
class BudgetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Permite retornar, actualizar o borrar un Presupuesto.
    """
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer