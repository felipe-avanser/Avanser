"""
Módulo: instructor.py
Descripción:
    Define las vistas API para la gestión de instructores dentro del sistema Avanser.
    Estas vistas permiten listar, crear, consultar, actualizar y eliminar instructores,
    respetando las jerarquías de roles definidas en el sistema.

Reglas jerárquicas:
    - Administrador del sistema:
        Puede crear, listar y editar cualquier instructor.
    - Coordinador de área:
        Puede listar y crear instructores de su área (control futuro por filtro).
    - Instructor:
        Solo puede ver su propio perfil (no crear ni editar a otros).
"""

from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from apps.instructor.models import Instructor
from apps.instructor.serializers.instructor import InstructorSerializer

User = get_user_model()


# ===========================================================
# === VISTA: LISTAR Y CREAR INSTRUCTORES ====================
# ===========================================================
class InstructorListCreateView(generics.ListCreateAPIView):
    """
    Vista para listar y crear instructores.

    - Administrador: puede ver y crear cualquier instructor.
    - Coordinador: puede listar y crear instructores (filtro por área en el futuro).
    - Instructor: solo puede ver su propio perfil.
    """
    queryset = Instructor.objects.select_related('usuario')
    serializer_class = InstructorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Filtra los instructores según el rol del usuario autenticado.
        """
        usuario = self.request.user
        rol = usuario.rol.nombre if usuario.rol else None

        if rol == "Administrador del sistema":
            return self.queryset
        elif rol == "Coordinador de área":
            # 🔹 En el futuro se puede filtrar por área específica
            return self.queryset
        elif rol == "Instructor":
            return self.queryset.filter(usuario=usuario)
        else:
            raise PermissionDenied("No tiene permiso para consultar instructores.")

    def perform_create(self, serializer):
        """
        Valida los permisos para crear un nuevo instructor.
        """
        usuario = self.request.user
        rol_creador = usuario.rol.nombre if usuario.rol else None

        if rol_creador not in ["Administrador del sistema", "Coordinador de área"]:
            raise PermissionDenied("No tiene permisos para crear instructores.")

        serializer.save()


# ===========================================================
# === VISTA: DETALLE, EDICIÓN Y ELIMINACIÓN ================
# ===========================================================
class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para obtener, actualizar o eliminar un instructor específico.
    Aplica las siguientes restricciones:
        - Administrador: puede modificar o eliminar cualquier instructor.
        - Coordinador: puede editar instructores (sin eliminar).
        - Instructor: solo puede ver su propio perfil.
    """
    queryset = Instructor.objects.select_related('usuario')
    serializer_class = InstructorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        Controla el acceso al objeto según el rol.
        """
        obj = super().get_object()
        usuario = self.request.user
        rol = usuario.rol.nombre if usuario.rol else None

        if rol == "Administrador del sistema":
            return obj
        elif rol == "Coordinador de área":
            return obj  # 🔹 Más adelante se podría validar por área
        elif rol == "Instructor":
            if obj.usuario != usuario:
                raise PermissionDenied("Solo puede acceder a su propio perfil.")
            return obj
        else:
            raise PermissionDenied("No tiene permiso para acceder a esta información.")

    def perform_destroy(self, instance):
        """
        Solo el Administrador puede eliminar instructores.
        """
        usuario = self.request.user
        if usuario.rol.nombre != "Administrador del sistema":
            raise PermissionDenied("No tiene permiso para eliminar instructores.")
        instance.delete()
