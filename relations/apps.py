from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RelationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relations'
    verbose_name = _('relations')
