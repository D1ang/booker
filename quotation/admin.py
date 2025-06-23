from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from typing import ClassVar
from .models import QuotationStatus, QuotationProgress, Quotation, QuotationRule


class ColorDisplayMixin:
    color_field_name = 'label_color'

    def color_display(self, obj: QuotationStatus) -> str:
        """Display the label color as a colored rectangle in the admin interface."""
        return format_html(
            '<div style="width: 20px; height: 20px; background-color: {}; border-radius: 50%;"></div>',
            getattr(obj, self.color_field_name),
        )

    color_display.short_description = _('label color')


@admin.register(QuotationStatus)
class QuotationStatusAdmin(admin.ModelAdmin, ColorDisplayMixin):
    list_display: ClassVar[list[str]] = ['label_description', 'color_display']


@admin.register(QuotationProgress)
class QuotationProgressAdmin(admin.ModelAdmin, ColorDisplayMixin):
    list_display: ClassVar[list[str]] = ['label_description', 'color_display']


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
