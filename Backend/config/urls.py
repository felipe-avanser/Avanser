"""
URL configuration for Avanser project.

Define las rutas principales del proyecto web y enlaza las aplicaciones registradas.
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

# Vista base (puede mostrar una plantilla HTML)
def home(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),          # Panel de administración de Django
    path('', home, name='home'),              # Página de inicio
    path('usuarios/', include('apps.usuario.urls')),
]

# Personalización del panel de administración
admin.site.site_header = "Panel de Administración Avanser"
admin.site.site_title = "Avanser"
admin.site.index_title = "Gestión de Avanser"
