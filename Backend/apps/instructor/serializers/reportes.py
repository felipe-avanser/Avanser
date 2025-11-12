from rest_framework import serializers
from apps.instructor.models import reporte as Reporte
from apps.aprendiz.models import Aprendiz
from apps.instructor.models.instructor import Instructor

class ReporteSerializer(serializers.ModelSerializer):
    aprendiz = 'AprendizSerializer'
    instructor = 'InstructorSerializer'

    aprendiz_id = serializers.PrimaryKeyRelatedField(
        queryset=Aprendiz.objects.all(), source='aprendiz', write_only=True
    )
    instructor_id = serializers.PrimaryKeyRelatedField(
        queryset=Instructor.objects.all(), source='instructor', write_only=True
    )

    class Meta:
        model = Reporte
        fields = '_all_'