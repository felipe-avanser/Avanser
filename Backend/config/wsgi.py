"""
WSGI config for Avanser project.

Este archivo expone la aplicación WSGI como una variable de nivel de módulo llamada ``application``.
WSGI (Web Server Gateway Interface) permite que Django maneje peticiones HTTP sincrónicas.
"""
import os
from django.core.wsgi import get_wsgi_application

# Indicar el archivo de configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Crear la aplicación WSGI
application = get_wsgi_application()
