from rest_framework import serializers
from transaction.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    """
    Permite acceder a lo datos basicos de una transaccion.
    """
    class Meta:
        model = Transaction
        fields = '__all__'

    def to_internal_value(self, data):
        """
        Permite inicializar los valores de la peticion
        """
        print("lo llama")
        data['user'] = self.context.get("request").parser_context["kwargs"]["user"]
        if 'category' in data:
            data['category_id'] = data['category']

        return super().to_internal_value(data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

class TransactionSummarySerializer(serializers.Serializer):
    """
    Permite acceder al monto total de transacciones por categoria.
    """
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
