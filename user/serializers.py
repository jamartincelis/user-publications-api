from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Permite acceder a lo datos basicos de un Usuario.
    """
    class Meta:
        model = User
        fields = ['id','optional_id', 'email']
