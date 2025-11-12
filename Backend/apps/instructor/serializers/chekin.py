from rest_framework import serializers
from apps.instructor.models import CheckInPeriodico

class CheckInItemSerializer(serializers.Serializer):
    aprendiz_id = serializers.IntegerField()
    estado_marcado = serializers.CharField(max_length=15)
    
class CheckInMasivoSerializer(serializers.Serializer):
    checkins = CheckInItemSerializer(many=True)
    
def create(self, validated_data):
    return validated_data