from django.contrib import admin
from .models import Status, Quotation, ProgressTypes


class StatusAdmin(admin.ModelAdmin):
    """
    """
    pass


class ProgressTypesAdmin(admin.ModelAdmin):
    """
    """
    pass


class QuotationAdmin(admin.ModelAdmin):
    """
    """
    list_display = ['quotation_number', 'status', 'date', 'expiration', 'relation', ]   #nog toe te voegen aan overzicht: user, Totaal exlc BTW, TOTAAL inc BTW, gefactureerd
    # list_filter = ["status", "date"]

    pass


admin.site.register(Status, StatusAdmin)
admin.site.register(ProgressTypes, ProgressTypesAdmin)
admin.site.register(Quotation, QuotationAdmin)
