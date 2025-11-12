from rest_framework import views, viewsets
from apps.competencia.models import competencia
from apps.competencia.serializers.competencia import CompetenciaSerializer

class CompetenciaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar las competencias.
    Proporciona operaciones CRUD para el modelo Competencia.
    """
    queryset = competencia.objects.all()
    serializer_class = CompetenciaSerializer