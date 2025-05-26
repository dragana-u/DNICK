from django.apps import AppConfig


class BalloonappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "balloonapp"

    def ready(self):
        from . import signals
