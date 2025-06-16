from django.contrib import admin
from typing import ClassVar
from django.utils.translation import gettext_lazy as _
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Admin interface for the Item model."""

    list_display: ClassVar[list[str]] = ['name', 'price', 'available']
    list_filter: ClassVar[list[str]] = ['available', 'created_at']
    search_fields: ClassVar[list[str]] = ['name', 'description']
    readonly_fields: ClassVar[list[str]] = ['added_by', 'created_at', 'updated_at']

    fieldsets: ClassVar[list[tuple[str, dict]]] = [
        (None, {'fields': ['name', 'description', 'price', 'available']}),
        (_('Metadata'), {'fields': ['added_by', 'created_at', 'updated_at']}),
    ]

    def save_model(self, request: any, obj: Item, _form: any, change: any) -> None:
        """Save the model instance with the current user."""
        if not change:
            obj.added_by = request.user
        obj.save()
