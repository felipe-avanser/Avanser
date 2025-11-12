from django.db import models
from apps.instructor.models import Instructor
from apps.aprendiz.models import Aprendiz
from django.utils import timezone

class AlertaAmarilla(models.Model):
    ESTADO_ACCION_CHOICES = [
    ('Pendiente', 'Pendiente'),
    ('Todo_bien', 'Todo bien'),
    ('Atencion_requerida', 'Atención requerida')
    ('Pospuesta', 'Pospuesta')
    ]
    aleAprendiz = models.ForeignKey('Aprendiz', on_delete=models.CASCADE, related_name='alertas_amarillas')
    
    aleInstructor = models.ForeignKey('Instructor', on_delete=models.SET_NULL, null=True, blank=True)
    
    fecha_deteccion = models.DateTimeField(default=timezone.now)
    
    descripcion = models.TextField(blank=True, null=True)
    
    estado_accion = models.CharField(max_length=20, choices=ESTADO_ACCION_CHOICES, default='Pendiente') 
    
    fecha_hasta = models.DateTimeField(null=True, blank=True, verbose_name="Fecha hasta")    
    
    class Meta:
        pass
        verbose_name = "Alerta Moderada (Amarilla)"
        
        def __str__(self):
            return f"Alerta Moderada para {self.aleAprendiz} el {self.fecha_deteccion.strftime('%Y-%m-%d')}"     