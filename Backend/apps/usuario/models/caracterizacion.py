from django.db import models
from django.contrib.auth.models import User

class Caracterizacion(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='encuesta')
    
    # --- DATOS PERSONALES ---
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=20)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()

    GENERO_CHOICES = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('O', 'Otro'),
    ]
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)

    ESTADO_CIVIL_CHOICES = [
        ('S', 'Soltero(a)'),
        ('C', 'Casado(a)'),
        ('U', 'Unión libre'),
        ('D', 'Divorciado(a)'),
        ('V', 'Viudo(a)'),
    ]
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL_CHOICES)

    NIVEL_EDUCATIVO_CHOICES = [
        ('P', 'Primaria'),
        ('B', 'Bachiller'),
        ('T', 'Técnico'),
        ('G', 'Tecnólogo'),
        ('U', 'Universitario'),
    ]
    nivel_educativo = models.CharField(max_length=1, choices=NIVEL_EDUCATIVO_CHOICES)

    grupo_etnico = models.CharField(max_length=50, blank=True, null=True)
    estrato = models.IntegerField(choices=[(i, str(i)) for i in range(0, 7)])
    barrio = models.CharField(max_length=100)
    comuna = models.CharField(max_length=2, choices=[(str(i), str(i)) for i in range(1, 10)])

    # --- BOOLEANOS ---
    tiene_hijos = models.BooleanField(default=False)
    acceso_internet = models.BooleanField(default=False)
    equipo_propio = models.BooleanField(default=False)
    responsable_hogar = models.BooleanField(default=False)
    apoyo_emocional = models.BooleanField(default=False)

    # --- SELECCIÓN ÚNICA ---
    ocupacion = models.CharField(
        max_length=20,
        choices=[
            ('E', 'Estudia'),
            ('T', 'Trabaja'),
            ('ET', 'Estudia y trabaja'),
            ('O', 'Otro'),
        ],
        blank=True, null=True
    )

    distancia_hogar = models.CharField(
        max_length=15,
        choices=[
            ('1-5', '1–5 km'),
            ('5-10', '5–10 km'),
            ('10+', 'Más de 10 km'),
        ],
        blank=True, null=True
    )

    # --- SELECCIÓN MÚLTIPLE ---
    motivos_dificultad = models.JSONField(
        blank=True, null=True,
        help_text="Lista de motivos: ['Económicos', 'Académicos', ...]"
    )

    tipo_dificultad = models.JSONField(
        blank=True, null=True,
        help_text="Ej: ['Económicas', 'Psicológicas']"
    )

    # --- PREGUNTAS ABIERTAS ---
    programa = models.CharField(max_length=150, blank=True, null=True)
    motivos_eleccion = models.TextField(blank=True, null=True)
    apoyos_necesarios = models.TextField(blank=True, null=True)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Encuesta de {self.nombres} {self.apellidos}"
