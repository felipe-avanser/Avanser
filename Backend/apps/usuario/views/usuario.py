from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from apps.usuario.serializers.usuario import RegistroUsuarioSerializer


User = get_user_model()

class RegistroUsuarioView(generics.CreateAPIView):
    """
    Vista para registrar usuarios de forma jerárquica.
    - El desarrollador crea al administrador.
    - El administrador crea coordinadores y funcionarios de bienestar.
    - El coordinador crea instructores.
    - Los aprendices se crean automáticamente desde la caracterización.
    """
    queryset = User.objects.all()
    serializer_class = RegistroUsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]  # solo usuarios logueados pueden crear otros

    def perform_create(self, serializer):
        creador = self.request.user
        rol_creador = creador.rol.nombre  # Asumiendo que tu modelo Usuario tiene campo "rol"

        nuevo_rol = serializer.validated_data.get('rol')

        # Validación jerárquica
        if rol_creador == "Administrador del sistema":
            if nuevo_rol.nombre not in ["Coordinador de área", "Funcionario de bienestar"]:
                raise PermissionDenied("Solo puede crear coordinadores o funcionarios de bienestar.")
        elif rol_creador == "Coordinador de área":
            if nuevo_rol.nombre != "Instructor":
                raise PermissionDenied("Solo puede crear instructores.")
        elif rol_creador in ["Instructor", "Funcionario de bienestar", "Aprendiz"]:
            raise PermissionDenied("No tiene permisos para crear usuarios.")

        # Guardar el usuario si pasa las validaciones
        serializer.save()
