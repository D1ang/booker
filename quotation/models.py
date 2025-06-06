from django.db import models
from django.utils.translation import gettext_lazy as _
from relation.models import Relation


class LabelDescription(models.Model):
    """Abstract base model with description and colour fields."""

    description = models.CharField(max_length=20, verbose_name=_('description'))
    colour = models.CharField(max_length=10, default='Green', verbose_name=_('colour'))

    class Meta:
        abstract = True
        verbose_name = _('Label description')

    def __str__(self) -> str:
        return self.description


class Status(LabelDescription):
    """Quotation status with colour labels."""

    class Meta:
        verbose_name = _('Status')
        verbose_name_plural = _('Statuses')


class Progress(LabelDescription):
    """Quotation progress types."""

    class Meta:
        verbose_name = _('Progress')
        verbose_name_plural = _('Progress')


class Quotation(models.Model):
    """Quotation details connections with status and relations."""

    quotation_number = models.CharField(max_length=12, unique=True, blank=True, verbose_name=_('quotation number'))
    relation = models.ForeignKey(Relation, on_delete=models.CASCADE, verbose_name=_('relation'))
    status = models.ForeignKey(Status, null=False, blank=False, on_delete=models.CASCADE, verbose_name=_('status'))
    progress_type = models.ForeignKey(Progress, on_delete=models.CASCADE, verbose_name=_('progress'))
    date = models.DateField(verbose_name=_('date'))
    expiration = models.DateField(verbose_name=_('expiration'))
    note = models.CharField(max_length=250, blank=True, verbose_name=_('note'))

    class Meta:
        verbose_name = _('Quotation')

    def __str__(self) -> str:
        return self.quotation_number

    def save(self, *args: object, **kwargs: object) -> None:
        """Create a quotation number based on: `YYYY-OF-INT` when saved."""
        if not self.quotation_number:
            year = str(self.date)
            prefix = f'{year[:4]}-OF-'

            self.quotation_number = f'{prefix}{self.pk:04d}'
        super().save(*args, **kwargs)


class QuotationRule(models.Model):
    """Quotation rules for the system."""

    quotation_rule = models.ForeignKey(Quotation, on_delete=models.CASCADE, verbose_name=_('quotation rule'))
    amount = models.IntegerField(verbose_name=_('amount'))
    description = models.CharField(max_length=50, verbose_name=_('description'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('price'))
    vat = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('VAT'))

    class Meta:
        verbose_name = _('Quotation rule')

    def __str__(self) -> str:
        return self.description
