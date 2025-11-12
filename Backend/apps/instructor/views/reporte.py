from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import status

from apps.instructor.models import reporte as Reporte
from apps.instructor.models.instructor import Instructor
from apps.aprendiz.models import Aprendiz
from apps.instructor.serializers.reportes import ReporteSerializer

class ReporteViewSet(viewsets.ModelViewSet):
    """
    ViewSet para el modelo Reporte.
    Proporciona operaciones CRUD para los reportes,
    incluyendo la creación, actualización, eliminación y listado.
    """

    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filtra los reportes según el instructor autenticado.
        """
        usuario_instructor = get_object_or_404(Instructor, usuario=self.request.user)
        return Reporte.objects.filter(instructor=usuario_instructor)