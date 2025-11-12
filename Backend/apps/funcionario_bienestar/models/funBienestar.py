from django.db import models
from apps.usuario.models import Usuario

class Funcionario(models.Model):
    funUsuario = models.OneToOneField(
        'Usuario', 
        on_delete=models.PROTECT, 
        related_name='funcionario_perfil',
        verbose_name="Usuario Asociado"
    )
    
    funCargo = models.CharField(
        max_length=50,
        default='Funcionario de Bienestar', 
        verbose_name="Cargo Especifico"
    )
    

    class Meta:
        verbose_name = "Funcionario de Bienestar"
        verbose_name_plural = "Funcionarios de Bienestar"

    def _str_(self):
        return f"{self.funUsuario.get_full_name()} ({self.funCargo})"