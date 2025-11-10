"""
Módulo: urls.py
Descripción:
    Define las rutas API del módulo Instructor.
"""

from django.urls import path
from apps.instructor.views.instructor import (
    InstructorListCreateView,
    InstructorDetailView
)

urlpatterns = [
    path('', InstructorListCreateView.as_view(), name='instructor-list-create'),
    path('<int:pk>/', InstructorDetailView.as_view(), name='instructor-detail'),
]
