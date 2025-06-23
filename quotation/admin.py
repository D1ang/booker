from django.contrib import admin
from typing import ClassVar
from .models import QuotationStatus, QuotationProgress, Quotation, QuotationRule


@admin.register(QuotationStatus)
class QuotationStatusAdmin(admin.ModelAdmin):
    list_display: ClassVar[list[str]] = ['label_description', 'label_colour']


@admin.register(QuotationProgress)
class QuotationProgressAdmin(admin.ModelAdmin):
    list_display: ClassVar[list[str]] = ['label_description', 'label_colour']


class QuotationInline(admin.TabularInline):
    model = QuotationRule
    extra = 1


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display: ClassVar[list[str]] = [
        'quote_number',
        'customer',
        'quote_date',
        'quote_expiration',
        'quote_progress',
        'quote_status',
    ]

    exclude: ClassVar[list[str]] = ['quote_number']
    inlines: ClassVar[list] = [QuotationInline]
