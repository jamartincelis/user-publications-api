from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status

from helpers.helpers import validate_date

from budget.serializers import BudgetSerializer
from budget.models import Budget


class BudgetsList(ListCreateAPIView):
    """
    Devuelve la lista de presupuestos del usuario
    """
    serializer_class = BudgetSerializer

    def get(self, request, user_id):
        date = validate_date(self.request.query_params.get('date_month'))
        if not date:
            return Response({'400': 'Invalid date format.'}, status=status.HTTP_400_BAD_REQUEST)
        budgets = Budget.objects.select_related('status').filter(
            user_id=user_id,
            budget_date__range=[date.start_of('month'), date.end_of('month')]
        )
        return Response(data=BudgetSerializer(budgets, many=True).data, status=status.HTTP_200_OK)

    def create(self, request, user_id):
        request.data['user_id'] = user_id
        instance = Budget.objects.create(**request.data)
        return Response(BudgetSerializer(instance).data, status=status.HTTP_201_CREATED)


class BudgetsByMonthAndCategory(ListAPIView):
    """
    Devuelve los presupuestos del usuario filtradas por mes y categoría
    """

    def get(self, request, user_id, category_id):
        date = validate_date(self.request.query_params.get('date_month'))
        if not date:
            return Response({'400': "Invalid date format."}, status=status.HTTP_400_BAD_REQUEST)
        budgets = Budget.objects.select_related('status', 'category').filter(
            user_id=user_id,
            category_id=category_id,
            budget_date__range=[date.start_of('month'), date.end_of('month')]
        )
        data = BudgetSerializer(budgets, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)


class BudgetDetail(RetrieveUpdateAPIView):
    """
    Permite retornar, actualizar o borrar un Presupuesto.
    """
    queryset = Budget.objects.select_related('status', 'category').all()
    serializer_class = BudgetSerializer
