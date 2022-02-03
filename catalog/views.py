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


class Catalog(RetrieveAPIView):
    """
    Devuelve los tipos de catalogos y sus catalogos filtrados por nombre.
    """
    serializer_class = CatalogSerializer
    lookup_field = 'name'
    queryset = CodeType.objects.prefetch_related('codes').all()
