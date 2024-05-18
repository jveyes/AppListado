from django.apps import AppConfig


class ApplistadoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AppListado'

    def ready(self):
        # Makes sure all signal handlers are connected
        from AppListado import handlers  # noqa