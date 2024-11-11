from django.db import models
from django.utils.translation import gettext_lazy as _


"""
ADD
LIST
KIND?
"""


class Status(models.Model):
    """
    Quotation status with
    colour labels.
    """
    description = models.CharField(max_length=20, verbose_name=_('description'))
    colour = models.CharField(max_length=10, default='Green', verbose_name=_('colour'))

    def __str__(self):
        return self.description


class Quotation(models.Model):
    """
    Quotation details connections
    with status and relations.
    """
    status = models.ForeignKey(Status, null=False, blank=False, on_delete=models.CASCADE)
    quotation_number = models.IntegerField()
    # relation = models.ForeignKey()
    relation_details = models.CharField(max_length=50)
    date = models.DateField()
    expiration = models.DateField()
    # quotation_template = models.ForeignKey()
    # email_template = models.ForeignKey()
    note = models.CharField(max_length=250)
    note_external = models.CharField(max_length=250)

    def __str__(self):
        return f"000{self.quotation_number}"
