"""
Utilidad de línea de comandos para tareas administrativas de Django.

Este archivo permite ejecutar comandos administrativos del proyecto Avanser,
como iniciar el servidor, crear migraciones, aplicar migraciones, crear
usuarios, ejecutar pruebas, entre otros.

"""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

def main():
    # Ruta base del backend
    BASE_DIR = Path(__file__).resolve().parent

    # Cargar variables de entorno (.env)
    env_path = BASE_DIR / '.env'
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)

    # Indicar el módulo de configuración del proyecto
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("No se pudo importar Django. ¿Está instalado y activo el entorno virtual?") from exc

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
