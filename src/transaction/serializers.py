from rest_framework import serializers

from catalog.serializers import ItemSerializer

from transaction.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    transaction_category = ItemSerializer(source='category', read_only=True)
    product_type = ItemSerializer(source='account_type', read_only=True)

    class Meta:
        model = Transaction
        fields = '__all__'


class TransactionSummarySerializer(serializers.Serializer):
    """
    Permite acceder al monto total de transacciones por categoria.
    """
    total_spend = serializers.IntegerField()
    num_transaction = serializers.IntegerField()
