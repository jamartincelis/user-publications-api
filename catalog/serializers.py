from rest_framework import serializers

from catalog.models import CodeType, Code


class CodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Code
        fields = ['id', 'name', 'metadata']


class CodeTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CodeType
        fields = fields = ['id', 'name']


class CatalogSerializer(serializers.ModelSerializer):

    codes = CodeSerializer(many=True)

    class Meta:
        model = CodeType
        fields = fields = ['id', 'name', 'metadata', 'codes']
