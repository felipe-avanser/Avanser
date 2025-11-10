from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.usuario.models import Rol
from apps.usuario.serializers import RolSerializer

class RolListView(generics.ListAPIView):
    """
    Retorna la lista de roles disponibles del sistema (solo lectura)
    Solo accesible para usuarios autenticados
    """
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [IsAuthenticated]


class RolDetailView(generics.RetrieveAPIView):
    """
    Retorna el detalle de un rol específico (solo lectura)
    """
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [IsAuthenticated]
