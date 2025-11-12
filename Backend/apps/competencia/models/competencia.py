from django.db import models
from apps.instructor.models import Instructor

class Competencia(models.Model):
    nombre = models.CharField(
        max_length=100,
        help_text="Nombre de la competencia."
    )

    descripcion = models.TextField(
        help_text="Descripción detallada de la competencia."
    )

    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE,
        related_name="competencias",
        help_text="Instructor responsable de la competencia."
    )

    def __str__(self):
        """
        Representación legible de la competencia.
        """
        return f"{self.nombre} - {self.instructor.nombre}"

    class Meta:
        verbose_name = "Competencia"
        verbose_name_plural = "Competencias"
        ordering = ["-fecha_creacion"]