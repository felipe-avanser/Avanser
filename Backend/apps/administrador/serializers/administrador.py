"""
Módulo: serializers.py
Descripción:
    Define los serializers para el modelo Administrador.
    Permite la serialización y deserialización de datos entre el modelo
    Administrador y las representaciones JSON utilizadas por la API REST.

Relaciones:
    - usuario: serializado con el modelo Usuario.
"""

from rest_framework import serializers
from apps.administrador.models import Administrador
from apps.usuario.models import Usuario
from apps.administrador.models.historial import HistorialAccion


class UsuarioSerializer(serializers.ModelSerializer):
    """
    Serializer básico para representar los datos del usuario asociado
    al administrador (solo lectura o resumen).
    """
    rol = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'rol']
        read_only_fields = ['id', 'username', 'rol']


class AdministradorSerializer(serializers.ModelSerializer):
    """
    Serializer principal del modelo Administrador.
    Permite listar, crear y actualizar registros de administradores,
    manteniendo la relación con el usuario del sistema.
    """

    # Relación anidada (solo lectura)
    usuario = UsuarioSerializer(read_only=True)

    # Campo para asignar usuario por su ID al crear/editar
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all(),
        source='usuario',
        write_only=True,
        help_text="ID del usuario asociado al administrador."
    )

    class Meta:
        model = Administrador
        fields = [
            'id',
            'nombre',
            'estado',
            'fecha_creacion',
            'usuario',      # lectura anidada
            'usuario_id',   # escritura
        ]
        read_only_fields = ['id', 'fecha_creacion']

    def validate_usuario(self, usuario):
        """
        Validación personalizada:
        Evita que un usuario que no tenga rol de Administrador del sistema
        sea asignado como administrador.
        """
        if usuario.rol and usuario.rol.nombre != 'Administrador del sistema':
            raise serializers.ValidationError(
                "El usuario seleccionado no tiene el rol de 'Administrador del sistema'."
            )
        return usuario

    def create(self, validated_data):
        """
        Crea un nuevo administrador.
        """
        return Administrador.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Actualiza los datos del administrador existente.
        """
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.estado = validated_data.get('estado', instance.estado)
        instance.usuario = validated_data.get('usuario', instance.usuario)
        instance.save()
        return instance

class HistorialAccionSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo HistorialAccion.
    Permite listar los registros de acciones realizadas por los administradores.
    """

    administrador = serializers.StringRelatedField(read_only=True)
    usuario_afectado = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = HistorialAccion
        fields = [
            'id',
            'accion',
            'descripcion',
            'fecha_accion',
            'administrador',
            'usuario_afectado',
        ]
        read_only_fields = ['id', 'fecha_accion']
