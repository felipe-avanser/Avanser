"""
Configuración de la aplicación 'instructor'.

Esta configuración permite que Django reconozca la app, 
asigne un nombre de etiqueta único (app_label) y defina un 
nombre descriptivo para el panel de administración.
"""

from django.apps import AppConfig


class InstructorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.instructor'        # Ruta completa del paquete
    label = 'instructor'            # app_label único
    verbose_name = 'Gestión de Instructores'
