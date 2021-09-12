from budget.models import Budget
from rest_framework import serializers
from catalog.serializers import CodeSerializer

class BudgetSerializer(serializers.ModelSerializer):
    """
    Permite acceder a lo datos basicos de un presupuesto.
    """
    category = CodeSerializer()
    class Meta:
        model = Budget
        fields = '__all__' 