"""
Módulo: instructor.py
Descripción:
    Define el modelo de Instructor dentro del sistema Avanser.
    Los instructores son usuarios con un rol específico que pueden tener
    responsabilidades académicas, de liderazgo o de coordinación.

Relaciones:
    - Usuario (OneToOne): relación directa con la tabla de usuarios.
    - Ficha (ManyToMany): fichas académicas que el instructor lidera o coordina.

Campos destacados:
    - especialidad: área técnica o profesional del instructor.
    - fun_cargo: función o cargo dentro del centro de formación.
    - es_coordinador: indica si tiene responsabilidades de coordinación académica.
    - es_lider: define si lidera fichas o procesos formativos específicos.
"""
from django.db import models
from apps.usuario.models.usuario import Usuario  


class Instructor(models.Model):
    """
    Modelo que representa a los instructores del sistema Avanser.
    """

    # === RELACIONES ===
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.PROTECT,
        related_name="perfil_instructor",
        help_text="Usuario asociado a este perfil de instructor."
    )

    # === DATOS PROFESIONALES ===
    especialidad = models.CharField(
        max_length=100,
        help_text="Área de especialidad técnica o profesional del instructor."
    )

    # === ROLES FUNCIONALES ===
    es_coordinador = models.BooleanField(
        default=False,
        verbose_name="¿Es Coordinador Académico?",
        help_text="Indica si el instructor cumple funciones de coordinación de área."
    )

    es_lider = models.BooleanField(
        default=False,
        verbose_name="¿Es Líder de Ficha?",
        help_text="Designa si este instructor lidera fichas o procesos formativos."
    )

    # === RELACIONES ADICIONALES ===
    fichas_a_cargo = models.ManyToManyField(
        'ficha.Ficha',
        related_name='lideres_asignados',
        verbose_name="Fichas a cargo",
        help_text="Fichas que el instructor lidera o supervisa."
    )

    # === REPRESENTACIÓN ===
    def __str__(self):
        """
        Representación legible del instructor, mostrando su rol funcional.
        """
        rol = "Coordinador" if self.es_coordinador else ("Líder" if self.es_lider else "Instructor")
        return f"{rol}: {self.usuario.username}"

    # === METADATOS ===
    class Meta:
        verbose_name = "Instructor"
        verbose_name_plural = "Instructores"
        ordering = ["usuario__username"]
        db_table = "instructor"
        constraints = [
            models.UniqueConstraint(
                fields=["usuario"],
                name="unique_usuario_instructor"
            )
        ]
