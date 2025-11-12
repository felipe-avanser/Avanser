"""
Módulo: administrador.py
Descripción:
    Define el modelo de Administrador dentro del sistema Avanser.
    Hereda del modelo CRUDAdmin (para las operaciones genéricas) 
    y se asocia directamente con el modelo Usuario mediante una relación OneToOne.

Relaciones:
    - usuario: referencia única al usuario con rol "Administrador del sistema".
"""

from django.db import models
from apps.usuario.models import Usuario
from apps.administrador.models.administrador import CRUDAdmin


class Administrador(models.Model, CRUDAdmin):
    """
    Representa al Administrador del sistema Avanser.
    Cada administrador está asociado a un único usuario del sistema
    con el rol "Administrador del sistema".
    """

    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        related_name="administrador",
        help_text="Usuario vinculado al rol de Administrador del sistema."
    )

    nombre = models.CharField(
        max_length=100,
        help_text="Nombre completo del administrador."
    )

    estado = models.BooleanField(
        default=True,
        help_text="Indica si el administrador está activo dentro del sistema."
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha y hora de creación del registro del administrador."
    )

    def __str__(self):
        """
        Representación legible del administrador.
        """
        return f"{self.nombre} ({self.usuario.username})"

    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"
        ordering = ["-fecha_creacion"]
        
