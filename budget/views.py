from budget.serializers import BudgetSerializer
from budget.models import Budget
from rest_framework import generics
from rest_framework.response import Response 
from rest_framework.decorators import api_view


@api_view(['GET'])
def budget_list(request, user):
    if request.method == 'GET':
        budgets = Budget.objects.filter(user=user)
        serializer = BudgetSerializer(budgets, many=True)
        return Response(serializer.data)

class BudgetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Permite retornar, actualizar o borrar un Presupuesto.
    """
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer