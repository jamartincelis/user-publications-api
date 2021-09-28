from catalog.models import Code
from helpers.helpers import validate_date
from user.models import User
from budget.serializers import BudgetSerializer, BudgetDetailSerializer
from budget.models import Budget
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, ListAPIView
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
        date = self.request.query_params.get('date_month')
        if not date:
            return Response({'400': "date_month it's required."}, status=status.HTTP_400_BAD_REQUEST)
        date = validate_date(date)
        if date is False:
            return Response({'400': 'Invalid date format.'}, status=status.HTTP_400_BAD_REQUEST)  
        budgets = budgets.filter(budget_date__range=[date.start_of('month'), date.end_of('month')])
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

class Category(ListAPIView):
    """
    Devuelve las transacciones del usuario filtradas por mes y categoría
    """
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    filterset_fields = ['date_month']

    def get(self, request, user, category):
        budgets = self.get_queryset().filter(user=user, category=category)
        date = self.request.query_params.get('date_month')
        if not date:
            return Response({'400': "date_month it's required."}, status=status.HTTP_400_BAD_REQUEST)
        date = validate_date(date)
        if date is False:
            return Response({'400': 'Invalid date format.'}, status=status.HTTP_400_BAD_REQUEST)
        budgets = budgets.filter(budget_date__range=[date.start_of('month'), date.end_of('month')])         
        data = BudgetSerializer(budgets, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)
        
class BudgetDetail(RetrieveUpdateAPIView):
    """
    Permite retornar, actualizar o borrar un Presupuesto.
    """
    queryset = Budget.objects.all()
    serializer_class = BudgetDetailSerializer
