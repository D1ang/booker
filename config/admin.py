from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from typing import ClassVar
from .models import GeneralLedgerAccount, LedgerGroup


@admin.register(LedgerGroup)
class LedgerGroupAdmin(admin.ModelAdmin):
    """Admin interface for the Ledger group model."""

    list_display: ClassVar[list[str]] = ['group_name']
    search_fields: ClassVar[list[str]] = ['group_name']


@admin.register(GeneralLedgerAccount)
class GeneralLedgerAccountAdmin(admin.ModelAdmin):
    """Admin interface for the GeneralLedgerAccount model."""

    list_display: ClassVar[list[str]] = ['code', 'description', 'category', 'group', 'active']
    list_filter: ClassVar[list[str]] = ['category', 'group', 'active']
    search_fields: ClassVar[list[str]] = ['code', 'description']
    fieldsets = (
        (None, {'fields': ('code', 'description', 'active')}),
        (_('Classification'), {'fields': ('category', 'group')}),
    )
