from django.db import models
from relations.models import Relation
from django.utils.translation import gettext_lazy as _


class Invoice(models.Model):
    """
    Invoice data
    """
    # base_invoice = models.
    relation = models.ForeignKey(Relation, on_delete=models.CASCADE)
    invoice_id = models.IntegerField()
    invoice_date = models.DateField()
    description = models.CharField(max_length=20, verbose_name=_('description'))
    payment_term = models.IntegerField()
    latest_payment_date = models.DateField()
    invoice_text = models.CharField(max_length=20, verbose_name=_('invoice text'))
    # invoice_template = models.
    # mail_template = models.
    collect_invoice_amount = models.BooleanField()
    invoice_to_bookkeeping = models.BooleanField()
    mutation_description = models.CharField(max_length=20, verbose_name=_('mutation description'))
    send_invoice = models.BooleanField()

# ADD inline products or services here!
