from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class Group(models.Model):
    """Model representing a group for general ledger accounts.
    Groups provide an additional level of classification for general ledger accounts.
    """

    name = models.CharField(_('name'), max_length=100, unique=True)

    def __str__(self):
        """Return the name of the group as its string representation."""
        return self.name

    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')
        ordering = ['name']


class GeneralLedgerAccount(models.Model):
    CATEGORY = (
        ('balance', _('Balance Sheet')),
        ('profit_loss', _('Profit and Loss')),
        ('payment', _('Payment Methods')),
        ('debtors', _('Debtors')),
        ('creditors', _('Creditors')),
        ('btw_rc', _('Btw r/c')),
        ('btw_overig', _('Btw af te dragen overig')),
        ('btw_laag', _('Btw af te dragen laag')),
        ('btw_hoog', _('Btw af te dragen hoog')),
        ('voorbelasting', _('Voorbelasting')),
    )

    # Categories that can only be used once
    UNIQUE_CATEGORIES = [
        'btw_rc',
        'btw_overig',
        'btw_laag',
        'btw_hoog',
        'voorbelasting',
    ]

    code = models.CharField(_('code'), max_length=10, unique=True)
    description = models.CharField(_('description'), max_length=255)
    category = models.CharField(
        choices=CATEGORY, max_length=20, verbose_name=_('category'))
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='accounts',
        verbose_name=_('group'),
        blank=True,
        null=True,
    )
    active = models.BooleanField(_('active'), default=True)

    def clean(self):
        """Validate that unique categories are only used once.
        """
        super().clean()

        if self.category in self.UNIQUE_CATEGORIES:
            # For new records or if category has changed
            query = GeneralLedgerAccount.objects.filter(category=self.category)

            # Exclude self when checking existing records
            if self.pk:
                query = query.exclude(pk=self.pk)

            if query.exists():
                category_display = dict(self.CATEGORY).get(self.category)
                raise ValidationError({
                    'category': _('The category "%(category)s" can only be assigned to one account.') % {
                        'category': category_display,
                    },
                })

    def save(self, *args, **kwargs):
        """Ensure validation is run before saving."""
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.code} - {self.description}'

    class Meta:
        verbose_name = _('General Ledger Account')
        verbose_name_plural = _('General Ledger Accounts')
        ordering = ['code']
