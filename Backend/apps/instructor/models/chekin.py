from django.db import models
from apps.instructor.models import Instructor
from apps.aprendiz.models import Aprendiz
from apps.ficha import Ficha 

class CheckInPeriodico(models.Model):
    ESTADO_CHOICES = [
        ('ACADEMICO', 'Problema Académico'),
        ('SOCIAL', 'Problema Social'),
        ('NORMAL', 'Todo Normal')
    ]

    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.PROTECT,
        related_name='checkins_realizados'
    )
    aprendiz = models.ForeignKey(
        Aprendiz,
        on_delete=models.PROTECT,
        related_name='checkins_recibidos'
    )

    ficha = models.ForeignKey(
        Ficha,
        on_delete=models.PROTECT,
        related_name='checkins_ficha'
    )

    estado_marcado = models.CharField(
        max_length=15,
        choices=ESTADO_CHOICES
    )
    
    fecha_checkin = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Check-In de {self.aprendiz} por {self.instructor}"