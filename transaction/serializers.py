from transaction.models import Transaction
from rest_framework import serializers

class TransactionSerializer(serializers.ModelSerializer):
    """
    Permite acceder a lo datos basicos de una transaccion.
    """
    class Meta:
        model = Transaction
        fields = ['id','amount', 'description','transaction_date','user','category'] 