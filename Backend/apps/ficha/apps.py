"""
Configuración de la aplicación 'ficha'.

Se encarga de administrar las fichas de formación SENA, 
las cuales agrupan aprendices bajo un mismo programa formativo.
"""

from django.apps import AppConfig


class FichaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.ficha'             # Ruta completa del paquete
    label = 'ficha'                 # app_label único
    verbose_name = 'Gestión de Fichas de Formación'
