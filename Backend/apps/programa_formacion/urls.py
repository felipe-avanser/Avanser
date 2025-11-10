from django.urls import path
from apps.programa_formacion.views import ProgramaFormacionViewSet

urlpatterns = [
    path('', ProgramaFormacionViewSet.as_view({'get': 'list', 'post': 'create'}), name='programa-formacion-list-create'),
    path('<int:pk>/', ProgramaFormacionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='programa-formacion-detail'),
]