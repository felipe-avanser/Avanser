
from django.db import models
from django.conf import settings

from apps.coordinador_area.models.area import Area

class AsignacionInstructorArea(models.Model):
    """
    Relación entre:
      - un instructor (Usuario con rol 'Instructor'),
      - un área,
      - un coordinador de área (Usuario con rol 'Coordinador').
    """

    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="asignaciones_areas_como_instructor",
        help_text="Usuario que tiene rol Instructor."
    )

    coordinador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="asignaciones_areas_como_coordinador",
        help_text="Usuario que tiene rol Coordinador de área."
    )

    area = models.ForeignKey(
        Area,
        on_delete=models.CASCADE,
        related_name="asignaciones_instructores"
    )

    fecha_asignacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "coordinador_area_asignacion_instructor_area"
        verbose_name = "Asignación de Instructor a Área"
        verbose_name_plural = "Asignaciones de Instructores a Áreas"
        # 👉 clave: no permitir instructor repetido en la misma área
        constraints = [
            models.UniqueConstraint(
                fields=["instructor", "area"],
                name="unique_instructor_area"
            )
        ]

    def __str__(self):
        return f"{self.instructor.username} → {self.area.nombre} ({self.coordinador.username})"
