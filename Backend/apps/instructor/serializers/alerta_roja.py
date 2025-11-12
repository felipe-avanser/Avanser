from rest_framework import serializers
from apps.aprendiz.serializers.aprendiz import AprendizSerializer
from apps.instructor.models.alerta_roja import AlertaRoja
from apps.aprendiz.models import Aprendiz

class AlertaRojaSerializer(serializers.ModelSerializer):
    aprendiz = AprendizSerializer(read_only=True)
    aprendiz_id = serializers.PrimaryKeyRelatedField(
        queryset=Aprendiz.objects.all(), source='aprendiz', write_only=True
    )

    class Meta:
        model = AlertaRoja
        fields = [
            'id',
            'aprendiz',
            'aprendiz_id',
            'motivo',
            'fecha_creacion',
            'activo',
        ]
        read_only_fields = ['id', 'fecha_creacion']