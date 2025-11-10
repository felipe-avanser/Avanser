from rest_framework import serializers
from apps.usuario.models import Caracterizacion

class CaracterizacionSerializer(serializers.ModelSerializer):
    """
    Serializer para registrar la caracterización del aprendiz.
    Crea automáticamente el usuario y calcula el nivel de riesgo.
    """
    # Estos campos se devuelven al finalizar el registro
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(read_only=True)
    nivel_riesgo = serializers.CharField(read_only=True)

    class Meta:
        model = Caracterizacion
        exclude = ['usuario', 'fecha_registro']

    def create(self, validated_data):
        # Crear instancia (el modelo maneja el usuario y el riesgo)
        caracterizacion = Caracterizacion.objects.create(**validated_data)

        # Agregar credenciales para mostrar al frontend
        caracterizacion.username = caracterizacion.usuario.username
        caracterizacion.password = caracterizacion.numero_identificacion

        return caracterizacion
