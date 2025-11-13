
from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.coordinador_area.models import Area, AsignacionInstructorArea

User = get_user_model()

class AsignacionInstructorAreaSerializer(serializers.ModelSerializer):
    instructor_username = serializers.CharField(source="instructor.username", read_only=True)
    coordinador_username = serializers.CharField(source="coordinador.username", read_only=True)
    area_nombre = serializers.CharField(source="area.nombre", read_only=True)

    class Meta:
        model = AsignacionInstructorArea
        fields = [
            "id",
            "instructor",
            "coordinador",
            "area",
            "fecha_asignacion",
            "instructor_username",
            "coordinador_username",
            "area_nombre",
        ]
        read_only_fields = ["id", "fecha_asignacion"]
