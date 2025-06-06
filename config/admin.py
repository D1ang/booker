from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import GeneralLedgerAccount, Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """Admin interface for the Group model."""

    list_display = ['name']
    search_fields = ['name']


@admin.register(GeneralLedgerAccount)
class GeneralLedgerAccountAdmin(admin.ModelAdmin):
    """Admin interface for the GeneralLedgerAccount model.

    Provides a customized view with filtered lists and search functionality
    for managing general ledger accounts.
    """

    list_display = ['code', 'description', 'category', 'group', 'active']
    list_filter = ['category', 'group', 'active']
    search_fields = ['code', 'description']
    fieldsets = (
        (None, {
            'fields': ('code', 'description', 'active'),
        }),
        (_('Classification'), {
            'fields': ('category', 'group'),
        }),
    )
