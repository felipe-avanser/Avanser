from django.db import models
from apps.usuario.models import Usuario 
from apps.ficha.models import Ficha

class Aprendiz(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.PROTECT, related_name="perfil_aprendiz")
    ficha = models.ForeignKey(
        Ficha,
        on_delete=models.PROTECT, 
        related_name='aprendices', 
        verbose_name="Ficha de Formación"
    )
    activo = models.BooleanField(
        default=True,
        verbose_name="Activo/Inactivo"
    )
    
    def _str_(self):
        return f"Aprendiz: {self.usuario.username}"