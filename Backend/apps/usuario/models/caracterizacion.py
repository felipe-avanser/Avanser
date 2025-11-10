import pandas as pd
from django.db import models, transaction
from django.contrib.auth import get_user_model
from apps.usuario.models import Rol

User = get_user_model()

class Caracterizacion(models.Model):
    """
    Contiene los datos de caracterización del aprendiz.
    """
    # Relación con el usuario creado automáticamente
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='caracterizacion')

    # === DATOS PERSONALES ===
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    numero_identificacion = models.CharField(max_length=20, unique=True)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=20)
    estado_civil = models.CharField(max_length=20)
    nivel_educativo = models.CharField(max_length=50)
    grupo_etnico = models.CharField(max_length=50)
    estrato = models.PositiveSmallIntegerField()
    barrio = models.CharField(max_length=100)
    comuna = models.CharField(max_length=10)
    ocupacion = models.CharField(max_length=50)
    tiene_hijos = models.BooleanField(default=False)
    cantidad_hijos = models.CharField(max_length=20, blank=True, null=True)

    # === CONTEXTO FAMILIAR Y SOCIAL ===
    con_quien_vive = models.CharField(max_length=50)
    cabeza_hogar = models.CharField(max_length=50)
    tipo_vivienda = models.CharField(max_length=50)
    num_personas_hogar = models.CharField(max_length=20)
    acceso_internet = models.BooleanField(default=False)
    equipo_propio = models.BooleanField(default=False)
    responsable_hogar = models.BooleanField(default=False)
    apoyo_formacion = models.BooleanField(default=False)
    apoyo_emocional = models.BooleanField(default=False)

    # === UBICACIÓN Y TRANSPORTE ===
    distancia_centro = models.CharField(max_length=20)
    medio_transporte = models.CharField(max_length=50)
    tiempo_desplazamiento = models.CharField(max_length=30)
    dificultad_transporte = models.BooleanField(default=False)
    costo_transporte = models.BooleanField(default=False)

    # === ASPECTOS ACADÉMICOS ===
    programa = models.CharField(max_length=150)
    motivo_programa = models.TextField(blank=True, null=True)
    apoyos_necesarios = models.TextField(blank=True, null=True)
    ha_pensado_dejar = models.BooleanField(default=False)
    motivos_dificultad = models.TextField(blank=True, null=True)
    apoyos_externos = models.BooleanField(default=False)
    apoyos_suficientes = models.BooleanField(default=False)
    jornada = models.CharField(max_length=20)
    dificultades_actuales = models.CharField(max_length=100)
    etapa_dificil = models.CharField(max_length=50)
    apoyo_necesario = models.CharField(max_length=50)
    horas_estudio_fuera = models.CharField(max_length=20)
    prob_finalizacion = models.CharField(max_length=20)

    # === SALUD Y BIENESTAR ===
    afiliacion_eps = models.BooleanField(default=False)
    condicion_salud = models.CharField(max_length=200, blank=True, null=True)
    condicion_psicologica = models.BooleanField(default=False)
    apoyo_psicologico = models.BooleanField(default=False)
    necesita_apoyo_salud = models.BooleanField(default=False)
    cambios_emocionales = models.BooleanField(default=False)
    actividad_fisica = models.CharField(max_length=20)
    ansiedad_estres = models.CharField(max_length=20)
    influencia_emociones = models.CharField(max_length=20)
    concentracion = models.CharField(max_length=20)

    # === ASPECTOS TECNOLÓGICOS ===
    tiene_dispositivo = models.BooleanField(default=False)
    dificultad_internet = models.BooleanField(default=False)
    comparte_dispositivo = models.CharField(max_length=50)

    # === ASPECTOS PSICOLÓGICOS Y EMOCIONALES ===
    presion_programa = models.BooleanField(default=False)
    decision_programa = models.CharField(max_length=200)
    piensa_ejercer = models.BooleanField(default=False)
    desea_apoyo_emocional = models.BooleanField(default=False)
    entorno_valora = models.BooleanField(default=False)
    entorno_positivo = models.BooleanField(default=False)
    victima_discriminacion = models.CharField(max_length=100)
    desplazamiento_conflicto = models.BooleanField(default=False)
    dano_familiar_conflicto = models.CharField(max_length=50)
    impacto_conflicto = models.CharField(max_length=50)
    dificultad_pedir_ayuda = models.CharField(max_length=50)
    influencia_conflicto_familiar = models.CharField(max_length=50)
    impacto_perdida = models.CharField(max_length=50)

    # === RESULTADOS ===
    nivel_riesgo = models.CharField(max_length=10, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def calcular_riesgo(self):
        """
        Cálculo simple de riesgo con pandas (base).
        """
        data = {
            'estrato': [self.estrato],
            'acceso_internet': [int(self.acceso_internet)],
            'equipo_propio': [int(self.equipo_propio)],
            'ha_pensado_dejar': [int(self.ha_pensado_dejar)],
            'apoyo_emocional': [int(self.apoyo_emocional)],
            'condicion_psicologica': [int(self.condicion_psicologica)],
            'dificultad_transporte': [int(self.dificultad_transporte)],
        }
        df = pd.DataFrame(data)

        puntaje = 0
        if df['estrato'][0] <= 2: puntaje += 2
        if df['acceso_internet'][0] == 0: puntaje += 1
        if df['equipo_propio'][0] == 0: puntaje += 1
        if df['ha_pensado_dejar'][0] == 1: puntaje += 2
        if df['apoyo_emocional'][0] == 0: puntaje += 1
        if df['condicion_psicologica'][0] == 1: puntaje += 2
        if df['dificultad_transporte'][0] == 1: puntaje += 1

        if puntaje <= 3:
            self.nivel_riesgo = "Bajo"
        elif puntaje <= 6:
            self.nivel_riesgo = "Medio"
        else:
            self.nivel_riesgo = "Alto"

    @transaction.atomic
    def save(self, *args, **kwargs):
        """
        Sobrescribe save para crear automáticamente el usuario aprendiz
        y calcular el nivel de riesgo.
        """
        # Crear usuario si no existe
        if not self.pk:
            primer_nombre = self.nombres.split()[0].lower()
            primer_apellido = self.apellidos.split()[0].lower()
            username = f"{primer_nombre}.{primer_apellido}"

            rol_aprendiz = Rol.objects.get(nombre__iexact="Aprendiz")

            user = User.objects.create_user(
                username=username,
                password=self.numero_identificacion,
                rol=rol_aprendiz
            )
            self.usuario = user

        # Calcular riesgo antes de guardar
        self.calcular_riesgo()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.nivel_riesgo})"
