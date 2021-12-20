from rest_framework import serializers

from catalog.models import CodeType, Code


class FilteredListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.exclude(name__in=('Sin categoría','Ignorar'))
        return super(FilteredListSerializer, self).to_representation(data)

class CodeSerializer(serializers.ModelSerializer):

    class Meta:
        list_serializer_class = FilteredListSerializer
        model = Code
        fields = ['id', 'name', 'metadata', 'description']

class CodeTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CodeType
        fields = fields = ['id', 'name']


class CatalogSerializer(serializers.ModelSerializer):

    codes = CodeSerializer(many=True)

    class Meta:
        model = CodeType
        fields = fields = ['id', 'name', 'codes']
