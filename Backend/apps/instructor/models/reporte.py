from django.db import models
from .instructor import Instructor
from apps.aprendiz.models import Aprendiz
from apps.ficha.models import Ficha 

class Reporte(models.Model):
    
    CATEGORIA_CHOICES = [
        ('AUSENCIA', 'Ausencia o Retardo'),
        ('RENDIMIENTO', 'Bajo Rendimiento Académico'),
        ('ACTITUDINAL', 'Problema Actitudinal o Disciplinario'),
        ('OTRO', 'Otro (Requiere Descripción Detallada)')
    ]
    
    instructor = models.ForeignKey(
        Instructor, 
        on_delete=models.PROTECT, 
        related_name='reportes_creados'
    )

    aprendiz = models.ForeignKey(
        Aprendiz, 
        on_delete=models.PROTECT,
        related_name='reportes_recibidos'
    )

    ficha = models.ForeignKey(
        Ficha, 
        on_delete=models.PROTECT,
        related_name='reportes_ficha'
    )
    
    descripcion = models.TextField(max_length=500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Reporte de {self.instructor.usuario.username} sobre {self.aprendiz.usuario.username} - {self.fecha_creacion.strftime('%d/%m/%Y')}"