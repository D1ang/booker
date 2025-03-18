from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Relation


class RelationAdmin(admin.ModelAdmin):
    """
    """
    fieldsets = [
        (
            None,
            {
                'fields': ['relation_type', 'code', 'company', 'company_number', 'contact', 'gender', 'salutation']
            }
        ),
        (
            _('Business address'),
            {
                'fields': ['adress', 'postal', 'city', 'country']
            }
        ),
        (
            _('Post address'),
            {
                'fields': ['post_adress', 'post_postal', 'post_city', 'post_country']
            }
        ),
        (
            _('Contact details'),
            {
                'fields': ['phone', 'mobile', 'mail', 'quotation_mail', 'reminders_mail', 'website']
            }
        ),
        (
            _('Payment details'),
            {
                'fields': ['iban', 'bic', 'btw', 'kind', 'general_ledger', 'term_of_payment', 'note', 'newsletters']
            }
        ),
    ]

    # enlarge field length for: 'relation type' & 'gender'
    def get_form(self, request, obj=None, **kwargs):
        form = super(RelationAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['relation_type'].widget.attrs['style'] = 'width: 21em;'
        form.base_fields['gender'].widget.attrs['style'] = 'width: 21em;'
        return form


admin.site.register(Relation, RelationAdmin)
