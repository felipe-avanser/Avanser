from django.db import models
from apps.aprendiz.models import Aprendiz
from apps.instructor.models import reporte as Reporte

class Citacion(models.Model):
    ESTADO_CHOICES = [
        ('BORRADOR', 'Borrador'),
        ('CREADA', 'Citación Creada'),
        ('ELIMINADA', 'Eliminada'), 
    ]
    
    aprendiz = models.ForeignKey(
        Aprendiz,
        on_delete=models.PROTECT,
        related_name='citaciones'
    )
    
    reporte = models.ForeignKey(
        Reporte,
        on_delete=models.SET_NULL, 
        blank=True
    )
    
    fecha_hora = models.DateTimeField(
        verbose_name="Fecha y Hora de Citación"
    )

    motivo = models.TextField(
        verbose_name="Motivo de la Citación"
    )


    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default='BORRADOR', 
        verbose_name="Estado de la Citación"
    )
    
    
    def _str_(self):
        return f"Citación a {self.aprendiz.nombre} ({self.estado})"

    class Meta:
        verbose_name = "Citación a Comité"
        verbose_name_plural = "Citaciones a Comités"