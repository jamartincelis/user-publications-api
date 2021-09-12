from budget.serializers import BudgetSerializer
from budget.models import Budget
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status


class BudgetList(ListAPIView):
    """
    Devuelve la lista de presupuestos del usuario
    """
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def get(self, request, user):
        budgets = self.get_queryset().filter(user=user)
        serializer = BudgetSerializer(budgets, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class BudgetDetail(RetrieveUpdateDestroyAPIView):
    """
    Permite retornar, actualizar o borrar un Presupuesto.
    """
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer