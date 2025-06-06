from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class QuotationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quotation'
    verbose_name = _('Quotation')
