from rest_framework import viewsets, views, status
from rest_framework.response import Response
from apps.instructor.models.citacion import Citacion
from apps.instructor.serializers.citacion import CitacionSerializer
from rest_framework.decorators import action

class CitacionViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar las citaciones a aprendices.
    Proporciona operaciones CRUD para el modelo Citacion.
    """
    queryset = Citacion.objects.all()
    serializer_class = CitacionSerializer

    @action(detail=False, methods=['get'])
    def citas_por_aprendiz(self, request):
        """
        Obtiene todas las citaciones para un aprendiz específico.
        Parámetro de consulta: aprendiz_id
        """
        aprendiz_id = request.query_params.get('aprendiz_id')
        if not aprendiz_id:
            return Response(
                {"error": "Se requiere el parámetro aprendiz_id."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        citaciones = self.queryset.filter(aprendiz__id=aprendiz_id)
        serializer = self.get_serializer(citaciones, many=True)
        return Response(serializer.data)    
    
    def perform_create(self, serializer):
        """
        Guarda una nueva citación en la base de datos.
        """
        serializer.save()
        return super().perform_create(serializer)
    def perform_update(self, serializer):
        """
        Actualiza una citación existente en la base de datos.
        """
        serializer.save()
        return super().perform_update(serializer)
    def perform_destroy(self, instance):
        """
        Elimina una citación de la base de datos.
        """
        instance.delete()
        return super().perform_destroy(instance)
    
    def create(self, request, *args, **kwargs):
        """
        Crea una nueva citación.
        """
        return super().create(request, *args, **kwargs)
    def update(self, request, *args, **kwargs):
        """
        Actualiza una citación existente.
        """
        return super().update(request, *args, **kwargs)
    def destroy(self, request, *args, **kwargs):
        """
        Elimina una citación existente.
        """
        return super().destroy(request, *args, **kwargs)
    def list(self, request, *args, **kwargs):
        """
        Lista todas las citaciones.
        """
        return super().list(request, *args, **kwargs)
    def retrieve(self, request, *args, **kwargs):
        """
        Recupera una citación específica por su ID.
        """
        return super().retrieve(request, *args, **kwargs)
    