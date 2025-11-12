from rest_framework import serializers
from apps.aprendiz.models import Aprendiz
from apps.aprendiz.serializers.aprendiz import AprendizSerializer

class AprendizDestacadoSerializer(serializers.ModelSerializer):
    aprendiz = AprendizSerializer(read_only=True)
    aprendiz_id = serializers.PrimaryKeyRelatedField(
        queryset=Aprendiz.objects.all(), source='aprendiz', write_only=True
    )

    #segun lps datos de la caracterizacion el aprendiz se destacara por buen resultado academico o por habilidades blandas
    
    motivo_destacado = serializers.ChoiceField(
        choices=[
            ('academico', 'Buen resultado académico'),
            ('habilidades_blandas', 'Habilidades blandas destacadas')
        ],
        help_text="Motivo por el cual el aprendiz es destacado."
    )
    class Meta:
        model = Aprendiz
        fields = [
            'id',
            'aprendiz',
            'aprendiz_id',
            'motivo_destacado',
            'fecha_destacado',
        ]
        read_only_fields = ['id', 'fecha_destacado']