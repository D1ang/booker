from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Item(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_('item name'))
    description = models.TextField(blank=True, verbose_name=_('description'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('item price'))
    available = models.BooleanField(default=True, verbose_name=_('available'))

    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))

    def __str__(self) -> str:
        return self.name
