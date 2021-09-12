from transaction.models import Transaction
from rest_framework import serializers
from catalog.serializers import CodeSerializer

class TransactionSerializer(serializers.ModelSerializer):
    """
    Permite acceder a lo datos basicos de una transaccion.
    """
    category = CodeSerializer()
    class Meta:
        model = Transaction
        fields = '__all__'