from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.timetable'

    def ready(self):
        import backend.scul.signals
