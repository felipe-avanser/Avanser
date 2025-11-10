from django.urls import path
from apps.ficha.views.fichas import FichaViewSet

urlpatterns = [
    path('', FichaViewSet.as_view({'get': 'list', 'post': 'create'}), name='ficha-list-create'),
    path('<int:pk>/', FichaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='ficha-detail'),
    
]