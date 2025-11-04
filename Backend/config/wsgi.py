"""
Configuración WSGI para el proyecto Avanser.

Este archivo define la configuración necesaria para desplegar el proyecto
Django en servidores que utilizan la interfaz WSGI (Web Server Gateway Interface),
como Apache, Nginx + Gunicorn o mod_wsgi.

Expone una variable de módulo llamada ``application``, que actúa como el punto
de entrada para que el servidor web se comunique con la aplicación Django.

"""