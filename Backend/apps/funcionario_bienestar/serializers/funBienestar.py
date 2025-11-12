from rest_framework import serializers
from apps.usuario.serializers import UsuarioSerializer
from apps.funcionario_bienestar.models import Funcionario

class FuncionarioSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='funUsuario.email', read_only=True)
    nombre_completo = serializers.SerializerMethodField()
    
    class Meta:
        model = Funcionario
        fields = [
            'id', 
            'email', 
            'nombre_completo',
            'funCargo', 
            'funTelefono', 
            ]
        read_only_fields = ['id', 'email', 'funCargo']
        
        def get_nombre_completo(self, obj):
            return f"{obj.funUsuario.first_name} {obj.funUsuario.last_name}"