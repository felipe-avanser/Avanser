#modelos de rol 
from django.db import models

ROLES = [
    ('coordinador', 'Coordinador de área'),
    ('instructor', 'Instructor'),
    ('funcionario', 'Funcionario de Bienestar'),
    ('aprendiz', 'Aprendiz') #necesario para el control 
]
