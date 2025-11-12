from rest_framework import serializers
from apps.instructor.models.citacion import Citacion
from apps.aprendiz.models import Aprendiz

class CitacionSerializer(serializers.ModelSerializer):
    aprendiz = serializers.PrimaryKeyRelatedField(
        queryset=Aprendiz.objects.all(),
        help_text="ID del aprendiz al que se le realiza la citación."
    )

    motivo = serializers.CharField(
        max_length=255,
        help_text="Motivo de la citación."
    )

    fecha_citacion = serializers.DateTimeField(
        help_text="Fecha y hora programada para la citación."
    )

    class Meta:
        model = Citacion
        fields = [
            'id',
            'aprendiz',
            'motivo',
            'fecha_citacion',
            'creado_en',
        ]
        read_only_fields = ['id', 'creado_en']