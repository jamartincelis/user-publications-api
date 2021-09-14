from catalog.models import Code
from helpers.helpers import validate_date
from user.models import User
from budget.serializers import BudgetSerializer, BudgetDetailSerializer
from budget.models import Budget
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status


class BudgetList(ListCreateAPIView):
    """
    Devuelve la lista de presupuestos del usuario
    """
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def get(self, request, user):
        budgets = self.get_queryset().filter(user=user)
        serializer = BudgetSerializer(budgets, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        model = serializer.save()
        code=Code.objects.get(pk=request.data['category'])
        model.category = code
        model.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class BudgetDetail(RetrieveUpdateAPIView):
    """
    Permite retornar, actualizar o borrar un Presupuesto.
    """
    queryset = Budget.objects.all()
    serializer_class = BudgetDetailSerializer