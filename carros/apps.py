
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class CarrosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carros'
    verbose_name = _("Gestão de Carros")

    def ready(self):
        # O único papel aqui é importar os sinais quando o Django iniciar
        import carros.signals  # Certifique-se de que o arquivo signals.py existe


        from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Perfil

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def gerenciar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)
    else:
        # Garante que o perfil seja salvo se o User for atualizado
        if hasattr(instance, 'perfil'):
            instance.perfil.save()
