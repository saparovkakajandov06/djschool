# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BaseConfig(AppConfig):
    label = 'authuser'
    name = 'backend.authuser'
    verbose_name = _('Auth User')
