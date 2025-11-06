"""
ASGI config for Avanser project.

Este archivo expone la aplicación ASGI como una variable de nivel de módulo llamada ``application``.
ASGI (Asynchronous Server Gateway Interface) permite que Django maneje peticiones asíncronas.
"""
import os
from django.core.asgi import get_asgi_application

# Indicar a Django qué archivo de configuración usar
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Crear la aplicación ASGI
application = get_asgi_application()
