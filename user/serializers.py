from user.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """
    Permite acceder a lo datos basicos de un Usuario.
    """
    class Meta:
        model = User
        fields = ['id','optional_id', 'email'] 