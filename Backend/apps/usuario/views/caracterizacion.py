# apps/caracterizacion/views/caracterizacion.py
from rest_framework import generics, status
from rest_framework.response import Response
from apps.usuario.models import Caracterizacion
from apps.usuario.serializers import CaracterizacionSerializer


class CaracterizacionCreateView(generics.CreateAPIView):
    """
    Endpoint para registrar la caracterización del aprendiz.
    - Crea automáticamente el usuario con rol Aprendiz.
    - Calcula nivel de riesgo (bajo, medio o alto).
    - Devuelve credenciales generadas.
    """
    queryset = Caracterizacion.objects.all()
    serializer_class = CaracterizacionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        caracterizacion = serializer.save()

        data = {
            "mensaje": "Caracterización registrada exitosamente.",
            "usuario_creado": {
                "username": caracterizacion.username,
                "password": caracterizacion.password,
                "nivel_riesgo": caracterizacion.nivel_riesgo
            }
        }

        return Response(data, status=status.HTTP_201_CREATED)
