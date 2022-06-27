from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
   
    label = 'scul'
    name = 'backend.scul'
    verbose_name = _('School')

    def ready(self):
        import backend.scul.signals
