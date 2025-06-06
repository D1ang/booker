from django.contrib import admin
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Relation


@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    """Admin interface for managing business relations."""

    fieldsets = (
        (
            None,
            {'fields': ['relation_type', 'code', 'company', 'company_number', 'contact', 'gender', 'salutation']},
        ),
        (
            _('Business address'),
            {'fields': ['adress', 'postal', 'city', 'country']},
        ),
        (
            _('Post address'),
            {'fields': ['post_adress', 'post_postal', 'post_city', 'post_country']},
        ),
        (
            _('Contact details'),
            {'fields': ['phone', 'mobile', 'mail', 'quotation_mail', 'reminders_mail', 'website']},
        ),
        (
            _('Payment details'),
            {'fields': ['iban', 'bic', 'vat', 'kind', 'general_ledger', 'term_of_payment', 'note', 'newsletters']},
        ),
    )

    def get_form(self, request, obj=None, **kwargs) -> ModelForm:
        """Return a customized form for the admin interface.

        Parameters
        ----------
        request : HttpRequest
            The current request object
        obj : Model, optional
            The object being edited, or None for new objects
        **kwargs : dict
            Additional keyword arguments

        Returns
        -------
        ModelForm
            The customized form with modified widget attributes

        """
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['relation_type'].widget.attrs['style'] = 'width: 21em;'
        form.base_fields['gender'].widget.attrs['style'] = 'width: 21em;'
        return form
