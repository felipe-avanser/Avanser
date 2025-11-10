from rest_framework import viewsets, views
from apps.programa_formacion.models import ProgramaFormacion
from apps.programa_formacion.serializers import ProgramaFormacionSerializer

class ProgramaFormacionViewSet(viewsets.ModelViewSet):
    """
    ViewSet para el modelo ProgramaFormacion.
    Proporciona operaciones CRUD completas para los programas de formación.
    """
    queryset = ProgramaFormacion.objects.all()
    serializer_class = ProgramaFormacionSerializer