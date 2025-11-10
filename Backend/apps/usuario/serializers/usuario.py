from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.usuario.models import Rol

User = get_user_model()


class RegistroUsuarioSerializer(serializers.ModelSerializer):
    """
    Serializer para registrar nuevos usuarios en el sistema Avanser.
    Solo requiere:
        - username
        - password
        - rol (por nombre)
    """
    # Permitimos que el frontend envíe el nombre del rol (ej: "Instructor")
    rol = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'rol']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 6}
        }

    def validate_rol(self, value):
        """
        Valida que el rol ingresado exista y lo devuelve como instancia.
        """
        try:
            rol = Rol.objects.get(nombre=value)
        except Rol.DoesNotExist:
            raise serializers.ValidationError(f"El rol '{value}' no existe.")
        return rol

    def validate_username(self, value):
        """
        Evita crear usuarios duplicados.
        """
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("El nombre de usuario ya existe.")
        return value

    def create(self, validated_data):
        """
        Crea un nuevo usuario con contraseña encriptada y rol asignado.
        """
        rol = validated_data.pop('rol')           # instancia del modelo Rol
        password = validated_data.pop('password')

        user = User(**validated_data)
        user.rol = rol
        user.set_password(password)               # encripta la contraseña
        user.save()
        return user
