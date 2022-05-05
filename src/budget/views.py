from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status

from helpers.helpers import validate_date

from budget.serializers import BudgetSerializer, BudgetDetailSerializer
from budget.models import Budget


class BudgetList(ListCreateAPIView):
    """
    Devuelve la lista de presupuestos del usuario
    """
    serializer_class = BudgetSerializer

    def get_queryset(self):
        return Budget.objects.filter(user=self.kwargs['user'])

    def get(self, request, user):
        budgets = self.get_queryset()
        date = validate_date(self.request.query_params.get('date_month'))
        if not date:
            return Response({'400': "Invalid date format."}, status=status.HTTP_400_BAD_REQUEST)
        if budgets:
            budgets = budgets.filter(budget_date__range=[date.start_of('month'), date.end_of('month')])
        serializer = BudgetSerializer(budgets, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        request.data['user'] = self.kwargs['user']
        instance = Budget.objects.create(**request.data)
        return Response(BudgetSerializer(instance).data, status=status.HTTP_201_CREATED)


class Category(ListAPIView):
    """
    Devuelve los presupuestos del usuario filtradas por mes y categoría
    """

    def get(self, request, user, category):
        date = validate_date(self.request.query_params.get('date_month'))
        if not date:
            return Response({'400': "Invalid date format."}, status=status.HTTP_400_BAD_REQUEST)
        budgets = Budget.objects.filter(
            user=user,
            category=category,
            budget_date__range=[date.start_of('month'), date.end_of('month')]
        )
        data = BudgetSerializer(budgets, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)
        return Response('OK', status=status.HTTP_200_OK)


class BudgetDetail(RetrieveUpdateAPIView):
    """
    Permite retornar, actualizar o borrar un Presupuesto.
    """
    queryset = Budget.objects.all()
    serializer_class = BudgetDetailSerializer
