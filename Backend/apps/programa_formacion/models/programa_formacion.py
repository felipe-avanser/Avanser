from django.db import models

class ProgramaFormacion(models.Model):
    """
    Modelo que representa los programas de formación ofrecidos.
    """

    nombre = models.CharField(
        max_length=100,
        help_text="Nombre del programa de formación."
    )

    descripcion = models.TextField(
        help_text="Descripción detallada del programa de formación."
    )

    duracion_meses = models.IntegerField(
        help_text="Duración del programa en meses."
    )

    nivel_formacion = models.CharField(
        max_length=100,
        help_text="Nivel de formación del programa (e.g., Técnico, Tecnólogo, Profesional)."
    )
    modalidad = models.CharField(
        max_length=50,
        help_text="Modalidad del programa (e.g., Presencial, Virtual, Mixta)."
    )

    def __str__(self):
        """
        Representación legible del programa de formación.
        """
        return self.nombre

    class Meta:
        verbose_name = "Programa de Formación"
        verbose_name_plural = "Programas de Formación"
        ordering = ["nombre"]
        db_table = "programa_formacion"