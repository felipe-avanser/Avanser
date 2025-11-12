from rest_framework.decorators import api_view 
from rest_framework.response import Response
from datetime import timedelta
from django.utils import timezone
from django.db.models import Count
from apps.instructor.models.reporte import  Reporte
from apps.aprendiz.models.aprendiz import Aprendiz

DIAS_ALERTA = 7
REPORTES_MINIMOS = 3

@api_view(['GET'])
def detectar_alertas_rojas(request):
    """
    Detecta aprendices que deben recibir una alerta roja
    basada en la cantidad de reportes en un período de tiempo.
    """
    fecha_limite = timezone.now() - timedelta(days=DIAS_ALERTA)
    
    reportes_recientes = Reporte.objects.filter(
        fecha_creacion__gte=fecha_limite
    )
    
    aprendices_con_reportes = reportes_recientes.values('aprendiz').annotate(
        total_reportes=Count('id')
    ).filter(total_reportes__gte=REPORTES_MINIMOS)
    
    alertas_rojas = []
    for aprendiz_data in aprendices_con_reportes:
        aprendiz_id = aprendiz_data['aprendiz']
        total_reportes = aprendiz_data['total_reportes']
        
        aprendiz = Aprendiz.objects.get(id=aprendiz_id)
        alerta = {
            'aprendiz_id': aprendiz.id,
            'nombre_aprendiz': f"{aprendiz.nombre} {aprendiz.apellido}",
            'total_reportes': total_reportes,
            'mensaje': f"El aprendiz {aprendiz.nombre} {aprendiz.apellido} ha recibido {total_reportes} reportes en los últimos {DIAS_ALERTA} días."
        }
        alertas_rojas.append(alerta)
    
    return Response(alertas_rojas)