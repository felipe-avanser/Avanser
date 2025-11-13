
from rest_framework import serializers
from apps.coordinador_area.models import Area

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ["id", "nombre", "descripcion"]
