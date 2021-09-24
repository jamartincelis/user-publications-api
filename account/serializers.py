from rest_framework import serializers

from account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    """
    Permite acceder a lo datos basicos de un Usuario.
    """
    class Meta:
        model = Account
        fields = ['id', 'user']
