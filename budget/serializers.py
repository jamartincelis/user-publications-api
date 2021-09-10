from budget.models import Budget
from rest_framework import serializers

class BudgetSerializer(serializers.ModelSerializer):
    """
    Permite acceder a lo datos basicos de un equipo.
    """
    class Meta:
        model = Budget
        fields = '__all__' 