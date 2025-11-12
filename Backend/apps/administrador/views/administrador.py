"""
Módulo: views.py
Descripción:
    Vistas para el módulo de Administrador en el sistema Avanser.
    Permiten a los administradores gestionar los usuarios del sistema:
        - Crear, leer, actualizar y eliminar usuarios.
        - Filtrar usuarios por rol, ficha o número de documento.
        - Registrar acciones administrativas (como desactivaciones).

Restricciones:
    Solo los usuarios con el rol "Administrador del sistema" pueden acceder
    a estas vistas.
"""

from rest_framework import generics, status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from apps.usuario.models import Usuario, Rol
from apps.administrador.models import Administrador
from apps.usuario.serializers import RegistroUsuarioSerializer  # Serializer base de usuario
from apps.administrador.serializers import AdministradorSerializer
from apps.administrador.permissions import EsAdministradorSistema
from apps.administrador.models.historial import HistorialAccion  # modelo que crearemos después
from apps.administrador.serializers import HistorialAccionSerializer
from apps.administrador.models.historial import HistorialAccion


# ===============================================================
# 🔒 PERMISO PERSONALIZADO
# ===============================================================

class EsAdministradorSistema(IsAuthenticated):
    """
    Permite el acceso solo a usuarios con rol 'Administrador del sistema'.
    """
    def has_permission(self, request, view):
        return bool(
            super().has_permission(request, view)
            and hasattr(request.user, "rol")
            and request.user.rol
            and request.user.rol.nombre == "Administrador del sistema"
        )


# ===============================================================
# 👤 CRUD DE USUARIOS POR ADMINISTRADOR
# ===============================================================

class UsuarioListCreateView(generics.ListCreateAPIView):
    """
    Permite listar y crear usuarios dentro del sistema.
    Solo accesible por administradores del sistema.

    Funcionalidades:
        - Listar todos los usuarios.
        - Filtrar por rol, número de documento o ficha.
        - Crear nuevos usuarios.
    """
    serializer_class = RegistroUsuarioSerializer
    permission_classes = [EsAdministradorSistema]
    queryset = Usuario.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['rol__nombre', 'is_active']
    search_fields = ['username', 'email', 'first_name', 'last_name']

    def get_queryset(self):
        """
        Permite filtrar por rol, ficha o número de documento mediante parámetros.
        """
        queryset = super().get_queryset()
        rol = self.request.query_params.get('rol')
        documento = self.request.query_params.get('documento')
        ficha = self.request.query_params.get('ficha')

        if rol:
            queryset = queryset.filter(rol__nombre__icontains=rol)
        if documento:
            queryset = queryset.filter(username__icontains=documento)  # suponiendo que el username es el documento
        if ficha:
            queryset = queryset.filter(ficha__codigo__icontains=ficha)  # suponiendo relación con modelo Ficha

        return queryset


class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Permite consultar, actualizar o eliminar un usuario específico.
    Solo los administradores del sistema tienen acceso.
    """
    serializer_class = RegistroUsuarioSerializer
    permission_classes = [EsAdministradorSistema]
    queryset = Usuario.objects.all()

    def update(self, request, *args, **kwargs):
        """
        Actualiza información básica del usuario:
            - Correo
            - Rol
            - Estado (activo/inactivo)
        Si se desactiva un usuario, se registra la acción en el historial.
        """
        instance = self.get_object()
        data = request.data
        usuario_admin = request.user

        # === Actualización permitida ===
        correo = data.get("email", instance.email)
        rol_id = data.get("rol")
        estado = data.get("is_active", instance.is_active)

        instance.email = correo
        if rol_id:
            try:
                nuevo_rol = Rol.objects.get(id=rol_id)
                instance.rol = nuevo_rol
            except Rol.DoesNotExist:
                return Response({"error": "El rol especificado no existe."}, status=400)

        # === Registro de desactivación ===
        if not estado and instance.is_active:
            instance.is_active = False
            # Guardamos en historial
            HistorialAccion.objects.create(
                administrador=Administrador.objects.get(usuario=usuario_admin),
                usuario_afectado=instance,
                accion="Desactivación de usuario",
                descripcion=f"El administrador {usuario_admin.username} desactivó al usuario {instance.username}."
            )
        else:
            instance.is_active = estado

        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        """
        Elimina un usuario del sistema.
        Registra la acción en el historial de administradores.
        """
        instance = self.get_object()
        usuario_admin = request.user

        HistorialAccion.objects.create(
            administrador=Administrador.objects.get(usuario=usuario_admin),
            usuario_afectado=instance,
            accion="Eliminación de usuario",
            descripcion=f"El administrador {usuario_admin.username} eliminó al usuario {instance.username}."
        )

        instance.delete()
        return Response(
            {"mensaje": f"Usuario {instance.username} eliminado correctamente."},
            status=status.HTTP_204_NO_CONTENT
        )

class HistorialAccionListView(generics.ListAPIView):
    """
    Permite a los administradores consultar el historial de acciones realizadas
    sobre los usuarios del sistema.

    Funcionalidades:
        - Listar todo el historial
        - Filtrar por tipo de acción, usuario afectado o administrador
        - Ordenar por fecha de acción
    """
    serializer_class = HistorialAccionSerializer
    permission_classes = [EsAdministradorSistema]
    queryset = HistorialAccion.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['accion', 'administrador__usuario__username', 'usuario_afectado__username']
    search_fields = ['descripcion', 'accion']
    ordering_fields = ['fecha_accion']
    ordering = ['-fecha_accion']
