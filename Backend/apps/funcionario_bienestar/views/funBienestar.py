from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from apps.funcionario_bienestar.models import Funcionario
from apps.funcionario_bienestar.serializers.funBienestar import FuncionarioSerializer

class FuncionarioViewSet(viewsets.ViewSet):
    serializer_class = FuncionarioSerializer
    def list(self, request):
        try:
            perfil = get_object_or_404(Funcionario, funUsuario=request.user)
        except Funcionario.DoesNotExist:
            return Response({"detail": "Perfil de Funcionario de Bienestar no encontrado."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(perfil)
        return Response(serializer.data)
    
    def partial_update(self, request, pk=None):
        try:
            perfil = get_object_or_404(Funcionario, funUsuario=request.user)
        except Funcionario.DoesNotExist:
            return Response({"detail": "Perfil de Funcionario de Bienestar no encontrado."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(perfil, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)