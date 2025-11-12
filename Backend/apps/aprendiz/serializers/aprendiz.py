from rest_framework import serializers
from apps.aprendiz.models import Aprendiz  

class AprendizSerializer(serializers.ModelSerializer):
    """
    Serializer principal del modelo Aprendiz.
    Permite listar, crear y actualizar registros de aprendices,
    manteniendo la relación con el usuario y la ficha de formación.
    """

    class Meta:
        model = Aprendiz
        fields = [
            'id',
            'usuario',      # relación con el usuario
            'ficha',        # relación con la ficha de formación
            'activo',       # estado del aprendiz
        ]
        read_only_fields = ['id']   