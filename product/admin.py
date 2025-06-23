from django.contrib import admin
from typing import ClassVar
from django.utils.translation import gettext_lazy as _
from .models import ProductItem


@admin.register(ProductItem)
class ProductAdmin(admin.ModelAdmin):
    list_display: ClassVar[list[str]] = ['product_title', 'product_price', 'product_availability']
    list_filter: ClassVar[list[str]] = ['product_title', 'product_availability', 'product_created_at']
    search_fields: ClassVar[list[str]] = ['product_title', 'product_description', 'product_added_by']
    readonly_fields: ClassVar[list[str]] = ['product_added_by', 'product_created_at', 'product_updated_at']

    fieldsets: ClassVar[list[tuple[str, dict]]] = [
        (
            _('product').upper(),
            {'fields': ['product_title', 'product_description', 'product_price', 'product_availability']},
        ),
        (
            _('metadata').upper(),
            {'fields': ['product_added_by', 'product_created_at', 'product_updated_at']},
        ),
    ]

    def save_model(self, request: any, obj: ProductItem, _form: any, change: any) -> None:
        """Save the model instance with the current user."""
        if not change:
            obj.added_by = request.user
        obj.save()
