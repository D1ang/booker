from django.contrib import admin
from typing import ClassVar
from django.utils.translation import gettext_lazy as _
from .models import TermOfPayment, Relation


@admin.register(TermOfPayment)
class TermOfPaymentAdmin(admin.ModelAdmin):
    """Admin interface for managing terms of payment."""

    list_display: ClassVar[list[str]] = ['description', 'days', 'is_default']
    ordering: ClassVar[list[str]] = ['description']
    fields: ClassVar[list[str]] = ['description', 'days', 'footer', 'is_default']


@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    """Admin interface for managing business relations."""

    fieldsets = (
        (
            None,
            {'fields': ['relation_type', 'code', 'company', 'company_number', 'contact', 'gender', 'salutation']},
        ),
        (
            _('Business address'),
            {'fields': ['adress', 'postal', 'city', 'country']},
        ),
        (
            _('Post address'),
            {'fields': ['post_adress', 'post_postal', 'post_city', 'post_country']},
        ),
        (
            _('Contact details'),
            {'fields': ['phone', 'mobile', 'mail', 'quotation_mail', 'reminders_mail', 'website']},
        ),
        (
            _('Payment details'),
            {'fields': ['iban', 'bic', 'vat', 'kind', 'general_ledger', 'term_of_payment', 'note', 'newsletters']},
        ),
    )
