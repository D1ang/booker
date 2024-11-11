from django.contrib import admin
from .models import Status, Quotation


class StatusAdmin(admin.ModelAdmin):
    """
    """
    pass


class QuotationAdmin(admin.ModelAdmin):
    """
    """
    list_display = ['quotation_number', 'date', 'expiration', 'status']
    # list_filter = ["status", "date"]

    pass


admin.site.register(Status, StatusAdmin)
admin.site.register(Quotation, QuotationAdmin)
