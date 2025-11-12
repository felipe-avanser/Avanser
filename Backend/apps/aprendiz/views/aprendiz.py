from rest_framework import viewsets, views
from apps.aprendiz.models import Aprendiz
from apps.aprendiz.serializers.aprendiz import AprendizSerializer

class AprendizViewSet(viewsets.ModelViewSet):
    """
    ViewSet para el modelo Aprendiz.
    Proporciona operaciones CRUD para los aprendices,
    incluyendo la creación, actualización, eliminación y listado.
    """

    queryset = Aprendiz.objects.all()
    serializer_class = AprendizSerializer