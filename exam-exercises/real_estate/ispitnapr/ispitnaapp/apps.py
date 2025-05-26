from django.apps import AppConfig


class IspitnaappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ispitnaapp"

    def ready(self):
        from . import signals
