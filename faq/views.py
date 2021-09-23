from faq.serializers import FaqSerializer
from faq.models import Faq
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

class FaqList(ListAPIView):
    """
    Devuelve la lista de preguntas frecuentes
    """
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer

    def get(self, request):
        faqs = self.get_queryset()
        data = FaqSerializer(faqs, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)