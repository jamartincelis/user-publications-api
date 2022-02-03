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

    def get(self, request, name):
        try:
            code = CodeType.objects.prefetch_related('codes').get(name=name)
            return Response(data=CatalogSerializer(code).data, status=status.HTTP_200_OK)
        except CodeType.DoesNotExist:
            return Response('Not found.', status=status.HTTP_404_NOT_FOUND)
