"""
Configuración ASGI para el proyecto Avanser.

Este archivo define la configuración necesaria para que el proyecto Django
pueda ejecutarse en un entorno ASGI (Asynchronous Server Gateway Interface),
el cual permite manejar conexiones asíncronas, como WebSockets o tareas en tiempo real.

Expone la variable de módulo ``application``, que representa la instancia
ASGI utilizada por los servidores compatibles (por ejemplo, Uvicorn o Daphne)
para comunicarse con el proyecto Django.

"""