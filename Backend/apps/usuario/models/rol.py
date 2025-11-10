"""
Módulo: rol.py
Descripción:
    Define los roles base del sistema Avanser.
    Estos roles determinan los permisos y accesos a las funcionalidades del sistema.

Roles definidos por defecto:
    1. Administrador del sistema
    2. Instructor
    3. Coordinador de área
    4. Funcionario de bienestar
    5. Aprendiz
"""

from django.db import models

class Rol(models.Model):
    """
    Modelo que representa los diferentes roles del sistema.
    """

    # Definición explícita de los roles posibles (ENUM)
    ADMINISTRADOR = 'Administrador del sistema'
    INSTRUCTOR = 'Instructor'
    COORDINADOR = 'Coordinador de área'
    BIENESTAR = 'Funcionario de bienestar'
    APRENDIZ = 'Aprendiz'

    OPCIONES_ROL = [
        (ADMINISTRADOR, 'Administrador del sistema'),
        (INSTRUCTOR, 'Instructor'),
        (COORDINADOR, 'Coordinador de área'),
        (BIENESTAR, 'Funcionario de bienestar'),
        (APRENDIZ, 'Aprendiz'),
    ]

    nombre = models.CharField(
        max_length=50,
        unique=True,
        choices=OPCIONES_ROL,
        help_text="Rol asignado al usuario dentro del sistema."
    )

    descripcion = models.TextField(
        blank=True, null=True,
        help_text="Descripción general del rol y sus responsabilidades."
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
