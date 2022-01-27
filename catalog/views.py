from rest_framework.generics import ListAPIView, RetrieveAPIView

from catalog.models import CodeType, Code
from catalog.serializers import CodeTypeSerializer, CodeSerializer, CatalogSerializer
from rest_framework.response import Response
from rest_framework import status

class CodeTypeList(ListAPIView):

    serializer_class = CodeTypeSerializer
    queryset = CodeType.objects.all().order_by('name')


class CodeList(ListAPIView):

    serializer_class = CodeSerializer
    queryset = Code.objects.all().order_by('name')


class CatalogList(ListAPIView):

    serializer_class = CatalogSerializer
    queryset = CodeType.objects.prefetch_related('codes').all().order_by('name')


class Catalog(ListAPIView):
    """
    Devuelve los tipos de catalogos y sus catalogos filtrados por nombre.
    """
    queryset = CodeType.objects.all()
    serializer_class = CatalogSerializer
    filterset_fields = ['name']

    def get(self, request, name):
        codes = self.get_queryset().filter(name=name)
        data = CatalogSerializer(codes, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)