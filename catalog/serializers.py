from rest_framework import serializers

from catalog.models import CodeType, Code


class CodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Code
        fields = '__all__'


class CodeTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CodeType
        fields = '__all__'


class CatalogSerializer(serializers.ModelSerializer):

    codes = CodeSerializer(many=True)

    class Meta:
        model = CodeType
        fields = '__all__'
