from rest_framework import serializers
from apps.ficha.models import Ficha

class FichaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Ficha.
    Permite la lectura y escritura de información completa de la ficha de formación.
    """

    class Meta:
        model = Ficha
        fields = [
            'id',
            'instructor_lider',
            'numero_ficha',
            'programa_formacion',
            'instructor',
            'fecha_inicio',
            'fecha_fin',
            'estado',
        ]
        read_only_fields = ['id']