from django.apps import AppConfig

class UsuarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.usuario'     # ruta real del paquete
    label = 'usuario'         # 👈 ESTE ES EL app_label
    verbose_name = 'Gestión de Usuarios'
