"""
Módulo: rol
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
from django.contrib.auth.models import AbstractUser
from django.db import models
from .rol import Rol

class Usuario(AbstractUser):
    """
    Usuario minimalista para Avanser:
        - username (heredado)
        - password (heredado)
        - rol -> FK a Rol
    """
    # mantenemos los campos de AbstractUser (username, password, is_active, etc.)
    rol = models.ForeignKey(
        Rol,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='usuarios',
        help_text='Rol asignado al usuario (p. ej. Aprendiz, Instructor).'
    )

    def __str__(self):
        return f"{self.username} ({self.rol})"

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["username"]
