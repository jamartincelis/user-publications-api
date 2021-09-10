from user.models import User
from user.serializers import UserSerializer
from rest_framework import generics
from rest_framework.decorators import authentication_classes, permission_classes
 
@authentication_classes([])
@permission_classes([])
class UserList(generics.ListCreateAPIView):
    """
    Permite listar y crear usuarios.
    """
    serializer_class = UserSerializer
        
    def get_queryset(self):
        """
        Se realizan los filtros de acuerdo a los parámetros ingresados
        """        
        queryset = User.objects.all()
        return queryset
    
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Permite retornar, actualizar o borrar un Usuario.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer