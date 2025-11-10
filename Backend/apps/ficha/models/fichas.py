from django.db import models
from apps.programa_formacion.models import ProgramaFormacion
from apps.instructor.models import Instructor

class Ficha(models.Model):
    nombre = models.CharField(max_length=100)
    # Instructor principal
    instructor = models.ForeignKey(
        'instructor.Instructor',
        on_delete=models.CASCADE,
        related_name='fichas_asignadas'   # 👈 nombre único para el acceso inverso
    )
    # Instructor líder
    instructor_lider = models.ForeignKey(
        'instructor.Instructor',
        on_delete=models.CASCADE,
        related_name='fichas_lideradas'   # 👈 otro nombre único
    )

    def __str__(self):
        return self.nombre