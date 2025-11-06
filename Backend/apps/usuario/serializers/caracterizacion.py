from rest_framework import serializers
from apps.usuario.models import Caracterizacion


class CaracterizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caracterizacion
        fields = '__all__'
