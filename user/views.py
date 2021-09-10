from user.models import User
from user.serializers import UserSerializer
from rest_framework import generics
from rest_framework.response import Response

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Permite retornar, actualizar o borrar un Usuario.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer