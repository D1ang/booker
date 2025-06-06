from django.contrib import admin
from typing import ClassVar
from .models import Invoice


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    """Admin configuration for managing Invoices in the admin interface."""

    list_display: ClassVar[list[str]] = [
        'invoice_date',
        'invoice_id',
        'relation',
    ]
