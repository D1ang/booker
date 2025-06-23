from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class ProductItem(models.Model):
    product_title = models.CharField(max_length=50, unique=True, verbose_name=_('product title'))
    product_description = models.TextField(blank=True, verbose_name=_('product description'))
    product_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('product price'))
    product_availability = models.BooleanField(default=True, verbose_name=_('product available'))

    product_added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name=_('product added by'))
    product_created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('product created at'))
    product_updated_at = models.DateTimeField(auto_now=True, verbose_name=_('product updated at'))

    class Meta:
        verbose_name = _('Product item')
        verbose_name_plural = _('Product items')

    def __str__(self) -> str:
        return self.product_title
