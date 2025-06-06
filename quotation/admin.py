from django.contrib import admin
from typing import ClassVar
from .models import Progress, Quotation, QuotationRule, Status


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    """Admin configuration for managing Statuses in the admin interface."""

    list_display: ClassVar[list[str]] = ['description', 'colour']


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    """Admin configuration for managing Progress in the admin interface."""

    list_display: ClassVar[list[str]] = ['description', 'colour']


class QuotationInline(admin.TabularInline):
    model = QuotationRule
    extra = 1


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    """Admin configuration for managing Quotations in the admin interface."""

    list_display: ClassVar[list[str]] = [
        'quotation_number',
        'relation',
        'date',
        'expiration',
        'progress_type',
        'status',
    ]

    exclude: ClassVar[list[str]] = ['quotation_number']
    inlines: ClassVar[list] = [QuotationInline]
