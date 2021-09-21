from transaction.models import Transaction
from rest_framework import serializers
from catalog.serializers import CodeSerializer

class TransactionSerializer(serializers.ModelSerializer):
    """
    Permite acceder a lo datos basicos de una transaccion.
    """
    category = CodeSerializer(read_only=True)
    class Meta:
        model = Transaction
        fields = '__all__'

class TransactionDetailSerializer(serializers.ModelSerializer):
    """
    Permite acceder a lo datos basicos de una transaccion.
    """
    class Meta:
        model = Transaction
        fields = '__all__'

class TransactionSummarySerializer(serializers.Serializer):
    """
    Permite acceder al monto total de transacciones por categoria.
    """
    category = serializers.UUIDField(read_only=False)
    total_spend = serializers.IntegerField()
    num_transaction = serializers.IntegerField()

class MonthlyBalanceSerializer(serializers.Serializer):
    """
    Permite acceder al balance mensual por anio.
    """
    month_name = serializers.CharField()
    incomes = serializers.IntegerField()
    expenses = serializers.IntegerField()
    balance = serializers.IntegerField()
    year = serializers.CharField()