"""
Módulo: historial.py
Descripción:
    Define el modelo HistorialAccion, encargado de registrar todas las
    acciones realizadas por los administradores del sistema sobre los usuarios.

Acciones registradas:
    - Creación de usuario
    - Actualización de usuario
    - Desactivación
    - Eliminación
"""

from django.db import models
from apps.usuario.models import Usuario
from apps.administrador.models import Administrador


class HistorialAccion(models.Model):
    administrador = models.ForeignKey(
        Administrador,
        on_delete=models.CASCADE,
        related_name="acciones_realizadas",
        help_text="Administrador que realizó la acción."
    )

    usuario_afectado = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name="acciones_recibidas",
        help_text="Usuario sobre el cual se ejecutó la acción."
    )

    accion = models.CharField(
        max_length=100,
        help_text="Tipo de acción realizada (por ejemplo, desactivación, eliminación, actualización)."
    )

    descripcion = models.TextField(
        help_text="Detalle o contexto de la acción realizada."
    )

    fecha_accion = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha y hora en que se ejecutó la acción."
    )

    class Meta:
        verbose_name = "Historial de Acción"
        verbose_name_plural = "Historial de Acciones"
        ordering = ["-fecha_accion"]

    def __str__(self):
        return f"{self.accion} - {self.usuario_afectado.username} ({self.fecha_accion:%Y-%m-%d %H:%M})"
