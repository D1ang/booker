from django.db import models
from django.utils.translation import gettext_lazy as _


class TermOfPayment(models.Model):
    """Model representing a term of payment for business relations."""

    description = models.CharField(max_length=30, verbose_name=_('description'))
    days = models.IntegerField(verbose_name=_('days'))
    footer = models.TextField(max_length=250, verbose_name=_('footer'))
    is_default = models.BooleanField(default=False, verbose_name=_('is default'))

    class Meta:
        verbose_name = _('Term of Payment')
        verbose_name_plural = _('Terms of Payment')

    def __str__(self) -> str:
        return self.description

    def save(self, *args: object, **kwargs: object) -> None:
        """Set all other `is_default` to false if this one is set to true."""
        if self.is_default:
            TermOfPayment.objects.exclude(pk=self.pk).update(is_default=False)
        super().save(*args, **kwargs)


class Relation(models.Model):
    """Model representing a business relation with various details."""

    RELATION = (
        ('company', _('Company')),
        ('relation', _('Relation')),
    )

    GENDER = (
        ('male', _('Male')),
        ('female', _('Female')),
        ('department', _('Department')),
    )

    relation_type = models.CharField(choices=RELATION, max_length=50, verbose_name=_('relation type'))
    code = models.CharField(max_length=50, primary_key=True, unique=True, verbose_name=_('code'))
    company = models.CharField(max_length=50, verbose_name=_('company'))
    company_number = models.CharField(max_length=50, verbose_name=_('company number'))
    contact = models.CharField(max_length=50, verbose_name=_('contact'))
    gender = models.CharField(choices=GENDER, max_length=50, verbose_name=_('gender'))
    salutation = models.CharField(max_length=50, verbose_name=_('salutation'))

    # business address
    adress = models.CharField(max_length=50, verbose_name=_('adress'))
    postal = models.CharField(max_length=50, verbose_name=_('postal'))
    city = models.CharField(max_length=50, verbose_name=_('city'))
    country = models.CharField(max_length=50, verbose_name=_('country'))

    # post address
    post_adress = models.CharField(max_length=50, verbose_name=_('post adress'))
    post_postal = models.CharField(max_length=50, verbose_name=_('post postal'))
    post_city = models.CharField(max_length=50, verbose_name=_('post city'))
    post_country = models.CharField(max_length=50, verbose_name=_('post country'))

    # contact details
    phone = models.CharField(max_length=50, verbose_name=_('phone'))
    mobile = models.CharField(max_length=50, verbose_name=_('mobile'))
    mail = models.CharField(max_length=50, verbose_name=_('mail'))
    quotation_mail = models.CharField(max_length=50, verbose_name=_('quotation mail'))
    reminders_mail = models.CharField(max_length=50, verbose_name=_('reminders mail'))
    website = models.CharField(max_length=50, verbose_name=_('website'))

    # payment details
    iban = models.CharField(max_length=50, verbose_name=_('iban'))
    bic = models.CharField(max_length=50, verbose_name=_('bic'))
    vat = models.CharField(max_length=50, verbose_name=_('vat'))
    kind = models.CharField(max_length=50, verbose_name=_('kind'))
    general_ledger = models.CharField(max_length=50, verbose_name=_('general ledger'))
    term_of_payment = models.ForeignKey(TermOfPayment, on_delete=models.CASCADE, verbose_name=_('term of payment'))
    note = models.CharField(max_length=50, verbose_name=_('note'))
    newsletters = models.BooleanField(max_length=50, verbose_name=_('newsletters'))

    class Meta:
        verbose_name = _('Relation')
        verbose_name_plural = _('Relations')

    def __str__(self) -> str:
        return self.company
