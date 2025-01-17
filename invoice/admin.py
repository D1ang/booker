from django.contrib import admin
from .models import Invoice


class InvoiceAdmin(admin.ModelAdmin):
    """
    """
    list_display = ['invoice_date', 'invoice_id', 'relation',]


admin.site.register(Invoice, InvoiceAdmin)
