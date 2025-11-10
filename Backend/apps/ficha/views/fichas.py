from rest_framework import viewsets, views
from apps.ficha.models import Ficha
from apps.ficha.serializers import FichaSerializer

class FichaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para el modelo Ficha.
    Proporciona operaciones CRUD completas para las fichas de formación.
    """
    queryset = Ficha.objects.all()
    serializer_class = FichaSerializer  