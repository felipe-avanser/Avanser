from django.db import models
from django.utils import timezone
from apps.aprendiz.models import Aprendiz
from apps.instructor.models import Instructor
from apps.instructor.models import  reporte as Reporte

class AlertaRoja(models.Model):
    # Alerta Roja
    aleAprendiz = models.ForeignKey('Aprendiz', on_delete=models.CASCADE, related_name='alertas_criticas')
    aleInstructor = models.ForeignKey('Instructor', on_delete=models.SET_NULL, null=True, blank=True)
    fecha_deteccion = models.DateTimeField(default=timezone.now)
    descripcion = models.TextField(blank=True, null=True)
    atendida = models.BooleanField(default=False) 

    class Meta:
        verbose_name = "Alerta Crítica (Roja)"
        verbose_name_plural = "Alertas Críticas (Rojas)"

    def _str_(self):
        return f"Alerta Crítica para {self.aleAprendiz} el {self.fecha_deteccion.strftime('%Y-%m-%d')}"