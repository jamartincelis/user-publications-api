from faq.models import Faq
from rest_framework import serializers

class FaqSerializer(serializers.ModelSerializer):
    """
    Permite acceder a lo datos basicos de una pregunta frecuente.
    """
    class Meta:
        model = Faq
        fields = '__all__'
