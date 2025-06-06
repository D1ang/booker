from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models
from typing import ClassVar


class LedgerGroup(models.Model):
    """Model representing a group for general ledger accounts."""

    group_name = models.CharField(_('name'), max_length=100, unique=True)

    class Meta:
        verbose_name = _('Ledger Group')
        verbose_name_plural = _('Ledger groups')
        ordering: ClassVar[list[str]] = ['group_name']

    def __str__(self) -> str:
        return self.group_name


class GeneralLedgerAccount(models.Model):
    CATEGORY = (
        ('balance', _('Balance sheet')),
        ('profit_loss', _('Profit and loss')),
        ('payment', _('Payment Methods')),
        ('debtors', _('Debtors')),
        ('creditors', _('Creditors')),
        ('vat_current', _('VAT current account')),
        ('vat_other', _('VAT to be paid other')),
        ('vat_low', _('VAT to be paid low')),
        ('vat_high', _('VAT to be paid high')),
        ('input_tax', _('Input tax')),
    )

    # categories that can only be used once
    UNIQUE_CATEGORIES: ClassVar[list[str]] = [
        'vat_current',
        'vat_other',
        'vat_low',
        'vat_high',
        'input_tax',
    ]

    code = models.CharField(_('code'), max_length=10, unique=True)
    description = models.CharField(_('description'), max_length=255)
    category = models.CharField(choices=CATEGORY, max_length=20, verbose_name=_('category'))
    group = models.ForeignKey(LedgerGroup, null=True, on_delete=models.SET_NULL, verbose_name=_('group'))
    active = models.BooleanField(_('active'), default=True)

    class Meta:
        verbose_name = _('General Ledger Account')
        verbose_name_plural = _('General Ledger Accounts')
        ordering: ClassVar[list[str]] = ['code']

    def __str__(self) -> str:
        return f'{self.code} - {self.description}'

    def save(self, *args: object, **kwargs: object) -> None:
        """Ensure validation is run before saving."""
        self.full_clean()
        super().save(*args, **kwargs)

    def clean(self) -> None:
        """Validate that unique categories are only used once."""
        super().clean()

        if self.category in self.UNIQUE_CATEGORIES:
            # for new records or if category has changed
            query = GeneralLedgerAccount.objects.filter(category=self.category)

            # exclude self when checking existing records
            if self.pk:
                query = query.exclude(pk=self.pk)

            if query.exists():
                category_display = dict(self.CATEGORY).get(self.category)
                raise ValidationError(
                    {
                        'category': _('The category "%(category)s" can only be assigned to one account.')
                        % {'category': category_display},
                    },
                )
