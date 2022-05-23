from django import http

from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from catalog.serializers import CatalogSerializer, ItemSerializer
from catalog.models import Catalog, Item


class CatalogListApiView(ListAPIView):

    serializer_class = CatalogSerializer
    queryset = Catalog.objects.prefetch_related('items').all()


class CatalogApiView(APIView):

    catalog_separator = ','

    def get(self, request):
        # requiere refactor para no hacer N peticiones a base, hacer solo una
        # y manejar el resultado en memoria
        catalogs = self.request.query_params.get('catalog', None)
        if catalogs:
            data = {}
            for catalog in catalogs.split(self.catalog_separator):
                data[catalog] = ItemSerializer(
                    Item.objects.filter(catalog_id__catalog_name=catalog, active=True),
                    many=True
                ).data
            return Response(data, status=status.HTTP_200_OK)
        return Response('Catalog not found', status=status.HTTP_404_NOT_FOUND)


class ItemDetail(RetrieveUpdateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.filter(pk=self.kwargs['pk'])
