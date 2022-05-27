from rest_framework import serializers
from catalog.serializers import ItemSerializer
from budget.models import Budget


class BudgetSerializer(serializers.ModelSerializer):

    budget_status = ItemSerializer(source='status', read_only=True)
    budget_category = ItemSerializer(source='category', read_only=True)

    class Meta:
        model = Budget
        fields = '__all__'