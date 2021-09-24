from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView

from user.models import User
from user.serializers import UserSerializer


class CreateUserView(CreateAPIView):
    """
    Crea un usuario.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetail(RetrieveUpdateAPIView):
    """
    Obtiene o actualiza un usuario.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
