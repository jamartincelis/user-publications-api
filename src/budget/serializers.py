from rest_framework import serializers

from catalog.serializers import ItemSerializer

from budget.models import Budget


class BudgetSerializer(serializers.ModelSerializer):

    status_id = ItemSerializer()

    class Meta:
        model = Budget
        fields = '__all__'
