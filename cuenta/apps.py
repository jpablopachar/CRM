from django.apps import AppConfig


class CuentaConfig(AppConfig):
    name = 'cuenta'

    def ready(self):
        import cuenta.signals
