from django.urls import path
from apps.administrador.views.administrador import (
    UsuarioListCreateView,
    UsuarioDetailView,
    HistorialAccionListView
)

urlpatterns = [
    # CRUD de usuarios
    path('usuarios/', UsuarioListCreateView.as_view(), name='usuarios-list-create'),
    path('usuarios/<int:pk>/', UsuarioDetailView.as_view(), name='usuarios-detail'),

    # Historial de acciones
    path('historial/', HistorialAccionListView.as_view(), name='historial-list'),
]
