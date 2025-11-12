from rest_framework import serializers
from apps.aprendiz.models import Aprendiz
from apps.instructor.models.alerta_amarilla import AlertaAmarilla

class AlertaAmarillaSerializer(serializers.Serializer):
    accion=serializers.ChoiceField(
        choices=['Todo_bien', 'Atencion_requerida', 'Pospuesta'],
        required=True,
        help_text="Acción tomada respecto a la alerta amarilla."
    )