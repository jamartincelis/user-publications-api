from tip.models import Tip
from rest_framework import serializers

class TipSerializer(serializers.ModelSerializer):
    """
    Permite acceder a lo datos basicos de un consejo.
    """
    class Meta:
        model = Tip
        fields = '__all__'
