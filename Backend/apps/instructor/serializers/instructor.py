"""
Módulo: instructor_serializer.py
Descripción:
    Define los serializadores para el modelo Instructor.
    Permiten la lectura y escritura de información completa del instructor,
    reutilizando el serializer de usuario existente.
"""

from rest_framework import serializers
from apps.instructor.models import Instructor
from apps.usuario.serializers.usuario import RegistroUsuarioSerializer  # Reutilizamos el existente


class InstructorSerializer(serializers.ModelSerializer):
    """
    Serializador principal del modelo Instructor.
    Permite ver el usuario asociado y sus roles sin duplicar lógica.
    """

    usuario = RegistroUsuarioSerializer(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(
        source='usuario',
        queryset=Instructor._meta.get_field("usuario").remote_field.model.objects.all(),
        write_only=True,
        help_text="ID del usuario asociado a este instructor."
    )

    class Meta:
        model = Instructor
        fields = [
            'id',
            'usuario',
            'usuario_id',
            'especialidad',
            'es_coordinador',
            'es_lider',
        ]
        read_only_fields = ['id']

    def to_representation(self, instance):
        """
        Personaliza la salida para mostrar el rol funcional.
        """
        data = super().to_representation(instance)
        rol = "Coordinador" if instance.es_coordinador else (
            "Líder" if instance.es_lider else "Instructor"
        )
        data["rol_funcional"] = rol
        return data
