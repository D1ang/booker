from django.db import models
from django.utils.translation import gettext_lazy as _
from relation.models import Relation


class Invoice(models.Model):
    """Invoice model to store invoice details."""

    relation = models.ForeignKey(Relation, null=True, on_delete=models.SET_NULL)
    invoice_id = models.IntegerField()
    invoice_date = models.DateField()
    description = models.CharField(max_length=20, verbose_name=_('description'))
    payment_term = models.IntegerField()
    latest_payment_date = models.DateField()
    invoice_text = models.CharField(max_length=20, verbose_name=_('invoice text'))
    collect_invoice_amount = models.BooleanField()
    invoice_to_bookkeeping = models.BooleanField()
    mutation_description = models.CharField(max_length=20, verbose_name=_('mutation description'))
    send_invoice = models.BooleanField()

    def __str__(self) -> str:
        return self.invoice_id
