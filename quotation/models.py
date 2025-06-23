from django.db import models
from django.utils.translation import gettext_lazy as _
from relation.models import Relation
from product.models import ProductItem
from datetime import datetime, timedelta, date


class QuotationBaseLabel(models.Model):
    label_description = models.CharField(max_length=20, verbose_name=_('label description'))
    label_colour = models.CharField(max_length=10, default='Green', verbose_name=_('label colour'))

    class Meta:
        abstract = True
        verbose_name = _('Quotation base label')

    def __str__(self) -> str:
        return self.label_description


class QuotationStatus(QuotationBaseLabel):
    class Meta:
        verbose_name = _('Quotation status')
        verbose_name_plural = _('Quotation statuses')


class QuotationProgress(QuotationBaseLabel):
    class Meta:
        verbose_name = _('Quotation progress')
        verbose_name_plural = _('Quotation progress')


class Quotation(models.Model):
    quote_number = models.CharField(max_length=12, unique=True, blank=True, verbose_name=_('quotation number'))
    customer = models.ForeignKey(Relation, on_delete=models.CASCADE, verbose_name=_('customer'))
    quote_status = models.ForeignKey(QuotationStatus, on_delete=models.CASCADE, verbose_name=_('quote status'))
    quote_progress = models.ForeignKey(QuotationProgress, on_delete=models.CASCADE, verbose_name=_('quote progress'))
    quote_date = models.DateField(default=date.today, verbose_name=_('quotation date'))
    quote_expiration = models.DateField(
        default=datetime.today() + timedelta(days=30),
        verbose_name=_('quote expiration'),
    )
    quote_note = models.CharField(max_length=250, blank=True, verbose_name=_('quotation note'))

    class Meta:
        verbose_name = _('Quotation')

    def __str__(self) -> str:
        return self.quote_number

    def save(self, *args: object, **kwargs: object) -> None:
        """Create a quotation number based on: `YYYY-OF-INT` when saved."""
        is_new = self.pk is None
        super().save(*args, **kwargs)

        if is_new and not self.quotation_number:
            year = str(self.date.year)
            prefix = f'{year}-OF-'
            self.quotation_number = f'{prefix}{self.pk:04d}'
            super().save(update_fields=['quote_number'])  # update on second save


class QuotationRule(models.Model):
    quotation_rule = models.ForeignKey(Quotation, on_delete=models.CASCADE, verbose_name=_('quotation rule'))
    quotation_product = models.ForeignKey(
        ProductItem,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name=_('prefilled product'),
    )
    product_amount = models.IntegerField(verbose_name=_('product amount'))
    product_description = models.CharField(max_length=50, verbose_name=_('product description'))
    product_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('product price'))
    product_vat = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('product VAT'))

    class Meta:
        verbose_name = _('Quotation rule')

    def __str__(self) -> str:
        return self.product_description
