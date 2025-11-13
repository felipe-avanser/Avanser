
from django.db import models

class Area(models.Model):
    """
    Área académica o programa funcional al que pertenece un instructor.
    Ejemplos: ADSO, IA, Redes, etc.
    """
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "Áreas"
        ordering = ["nombre"]
        db_table = "coordinador_area_area"
