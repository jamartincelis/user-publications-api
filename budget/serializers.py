from rest_framework import serializers

from catalog.serializers import CodeSerializer

from budget.models import Budget


class BudgetSerializer(serializers.ModelSerializer):
    """
    Permite acceder a lo datos basicos de un presupuesto.
    """
    category = CodeSerializer(read_only=True)

    class Meta:
        model = Budget
        fields = '__all__' 


class BudgetDetailSerializer(serializers.ModelSerializer):
    """
    Permite editar los datos basicos de un presupuesto.
    """
    category = CodeSerializer(read_only=True)

    class Meta:
        model = Budget
        fields = '__all__' 
