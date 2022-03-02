from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HealthCheckApiView(APIView):
    def get(self, request):
        return Response('OK', status=status.HTTP_200_OK)


class SentryApiView(APIView):
    def get(self, request):
        print(1 / 0)
        return Response('OK', status=status.HTTP_200_OK)
