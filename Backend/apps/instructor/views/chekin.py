from rest_framework import viewsets, status, serializers 
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from django.db import transaction
from apps.instructor.models import CheckInPeriodico
from apps.aprendiz.models import Aprendiz 
from apps.instructor.models import Instructor
from apps.instructor.serializers import CheckInItemSerializer, CheckInMasivoSerializer 


class CheckInViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated] 
    serializer_class = CheckInItemSerializer 
    
    @action(detail=False, methods=['get'])
    def lista_aprendices(self, request):
        user = request.user
        try:
            instructor = Instructor.objects.get(usuario=user)
        except Instructor.DoesNotExist:
            return Response({"detail": "Usuario no es un instructor válido."}, status=status.HTTP_403_FORBIDDEN)
        
        fichas_a_cargo = instructor.fichas_a_cargo.all()
        aprendices = Aprendiz.objects.filter(ficha__in=fichas_a_cargo, activo=True)
        data = [{'id': a.id, 'nombre': a.nombre, 'ficha_id': a.ficha.id} for a in aprendices]
        return Response(data)
        
        
    @action(detail=False, methods=['post'])
    def registrar_masivo(self, request):
        serializer = CheckInMasivoSerializer(data=request.data) 
        serializer.is_valid(raise_exception=True)
        checkins_data = serializer.validated_data['checkins']
        
        try:
            instructor = Instructor.objects.get(usuario=request.user)
        except Instructor.DoesNotExist:
            return Response({"detail": "Usuario no es un instructor válido."}, status=status.HTTP_403_FORBIDDEN)
        
        registros = []
        
        with transaction.atomic():
            for item in checkins_data:
                aprendiz_id = item['aprendiz_id']
                estado = item['estado_marcado']

                try:
                    aprendiz = Aprendiz.objects.get(pk=aprendiz_id)
                except Aprendiz.DoesNotExist:
                    raise serializers.ValidationError(f"Aprendiz con ID {aprendiz_id} no encontrado.") 
                
                registro = CheckInPeriodico(
                    instructor=instructor,
                    aprendiz=aprendiz,
                    ficha=aprendiz.ficha, 
                    estado_marcado=estado
                )
                registros.append(registro)
                
        CheckInPeriodico.objects.bulk_create(registros)

        return Response({"detail": f"Registro masivo exitoso. {len(registros)} check-ins creados."}, 
                        status=status.HTTP_201_CREATED)