from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView

from account.models import Account
from account.serializers import AccountSerializer


class CreateAccountView(CreateAPIView):
    """
    Crea un usuario.
    """
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


class AccountDetail(RetrieveUpdateAPIView):
    """
    Obtiene o actualiza un usuario.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
