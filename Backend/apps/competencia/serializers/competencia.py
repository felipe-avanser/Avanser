from rest_framework import serializers
from apps.competencia.models import Competencia

class CompetenciaSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(
        max_length=100,
        help_text="Nombre de la competencia."
    )

    descripcion = serializers.CharField(
        help_text="Descripción detallada de la competencia."
    )

    instructor_id = serializers.PrimaryKeyRelatedField(
        queryset=Competencia.objects.all(),
        source='instructor',
        help_text="ID del instructor responsable de la competencia."
    )

    class Meta:
        model = Competencia
        fields = [
            'id',
            'nombre',
            'descripcion',
            'instructor_id',
            'fecha_creacion',
        ]
        read_only_fields = ['id', 'fecha_creacion']