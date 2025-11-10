"""
Configuración principal de Django para el proyecto Avanser.
Entorno: Desarrollo local con PostgreSQL y React frontend.
"""
from pathlib import Path
import os
from dotenv import load_dotenv

# RUTAS PRINCIPALES
BASE_DIR = Path(__file__).resolve().parent.parent

# Cargar variables de entorno
load_dotenv(BASE_DIR / '.env')

#SEGURIDAD
SECRET_KEY = os.getenv('SECRET_KEY', 'clave-insegura-en-desarrollo')
DEBUG = os.getenv('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

#APLICACIONES INSTALADAS
INSTALLED_APPS = [
    # Apps de Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps externas
    'rest_framework',
    'corsheaders',

    # Apps locales
    # 'apps.coordinador_area',
    # 'apps.funcionario_bienestar',
    # 'apps.instructor',
    'apps.usuario',
]

#MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#URLS / WSGI
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'


#TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],          # No usaremos plantillas personalizadas aqui 
        'APP_DIRS': True,    # Para que el admin funcione
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
] 

#BASE DE DATOS (PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),

        # Base de datos para tests automáticos (opcional)
        # 'TEST': {
        #     'NAME': os.getenv('DB_TEST_NAME', 'test_avanser'),
        # },
    }
}

#IDIOMA / ZONA HORARIA
LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True

# AUTENTICACIÓN Y VALIDACION DE CONTRASEÑAS
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ARCHIVOS ESTÁTICOS Y MEDIA
# Archivos estáticos mínimos — solo para que funcione el admin
STATIC_URL = '/static/'

# Archivos que suben los usuarios (fotos, documentos, etc.)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


#CONFIG ADICIONAL (utomáticamente agrega una clave primaria)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS CONFIG
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Puerto del frontend
]
CORS_ALLOW_CREDENTIALS = True

# REST FRAMEWORK CONFIG (JWT Authentication)
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}


#Registro de modelos 
AUTH_USER_MODEL = 'usuario.Usuario'

