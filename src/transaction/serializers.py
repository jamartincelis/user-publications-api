from rest_framework import serializers

from catalog.serializers import ItemSerializer

from transaction.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    transaction_category_status = ItemSerializer(source='category', read_only=True)

    class Meta:
        model = Budget
        fields = '__all__'
