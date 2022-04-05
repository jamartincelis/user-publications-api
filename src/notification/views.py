import notification
from notification.models import Notification
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from notification.serializers import NotificationSerializer

class NoticationList(ListAPIView):
    """
    Devuelve la lista de notificaciones.
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get(self, request):
        notifications = self.get_queryset()
        data = NotificationSerializer(notifications, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)