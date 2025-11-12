"""
URL configuration for the aplicación 'aprendiz'.

Define las rutas que exponen los endpoints relacionados con aprendices.
Cada vista debe estar definida en apps.aprendiz.views.
"""

from django.urls import path
from apps.aprendiz import views

urlpatterns = [
    path('aprendices/', views.AprendizViewSet.as_view({'get': 'list', 'post': 'create'}), name='aprendiz-list-create'),
    path('aprendices/<int:pk>/', views.AprendizViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='aprendiz-detail'),
]
