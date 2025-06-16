from django.contrib import admin
from typing import ClassVar
from django.utils.translation import gettext_lazy as _
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

    fieldsets: ClassVar[list[tuple[str, dict]]] = [
        (_('Account'), {'fields': ['code', 'description', 'active']}),
        (_('Classification'), {'fields': ['category', 'group']}),
    ]
