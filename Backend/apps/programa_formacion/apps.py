"""
Configuración de la aplicación 'programa_formacion'.

Administra los programas de formación del SENA, 
que luego se asocian con fichas e instructores.
"""

from django.apps import AppConfig


class ProgramaFormacionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.programa_formacion'  # Ruta completa del paquete
    label = 'programa_formacion'      # app_label único
    verbose_name = 'Gestión de Programas de Formación'
