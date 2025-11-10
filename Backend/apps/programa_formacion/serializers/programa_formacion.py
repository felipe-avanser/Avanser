from rest_framework import serializers
from apps.programa_formacion.models import ProgramaFormacion

class ProgramaFormacionSerializer(serializers.ModelSerializer): 
    """
    Serializador para el modelo ProgramaFormacion.
    Permite la lectura y escritura de información completa del programa de formación.
    """

    class Meta:
        model = ProgramaFormacion
        fields = [
            'id',
            'nombre',
            'descripcion',
            'duracion_meses',
            'nivel_formacion',
            'modalidad',
        ]
        read_only_fields = ['id']