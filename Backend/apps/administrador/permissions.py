"""
Módulo: permissions.py
Descripción:
    Define permisos personalizados para el módulo de Administrador en el sistema Avanser.
    Se asegura de que solo los usuarios con el rol 'Administrador del sistema'
    puedan acceder a las vistas administrativas.
"""

from rest_framework.permissions import BasePermission


class EsAdministradorSistema(BasePermission):
    """
    Permite acceso únicamente a los usuarios con el rol 'Administrador del sistema'.
    """

    def has_permission(self, request, view):
        # Verifica que el usuario esté autenticado y tenga rol de administrador
        user = request.user
        return bool(
            user.is_authenticated
            and hasattr(user, "rol")
            and user.rol
            and user.rol.nombre == "Administrador del sistema"
        )

    def has_object_permission(self, request, view, obj):
        # Igual que arriba, para objetos específicos
        return self.has_permission(request, view)
