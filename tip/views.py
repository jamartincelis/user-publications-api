from tip.models import Tip
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from tip.serializers import TipSerializer

class TipList(ListAPIView):
    """
    Devuelve la lista de consejos.
    """
    queryset = Tip.objects.all()
    serializer_class = TipSerializer

    def get(self, request):
        tips = self.get_queryset()
        data = TipSerializer(tips, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)