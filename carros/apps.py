from django.apps import AppConfig
from django.carros.singals import create_profile



class CarrosConfig(AppConfig):
    name = 'carros'
class CarrosConfig(AppConfig):
    name = 'carros'
    class Meta:
        verbose_name = "Carros"

    def ready(self):
        import carros.signals  # Importa sinais para criar perfis automaticamente