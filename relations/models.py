from django.db import models


class Relation(models.Model):
    """
    """
    RELATION = (
        ('company', 'Company'),
        ('relation', 'Relation'),
    )

    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('department', 'department'),
    )
    relation_type = models.CharField(choices=RELATION, max_length=50)
    code = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    company_number = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER, max_length=50)
    salutation = models.CharField(max_length=50)

    # business address
    adress = models.CharField(max_length=50)
    postal = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    # post address
    post_adress = models.CharField(max_length=50)
    post_postal = models.CharField(max_length=50)
    post_city = models.CharField(max_length=50)
    post_country = models.CharField(max_length=50)

    # contact details
    phone = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    quotation_mail = models.CharField(max_length=50)
    reminders_mail = models.CharField(max_length=50)
    website = models.CharField(max_length=50)

    # payment details
    iban = models.CharField(max_length=50)
    bic = models.CharField(max_length=50)
    btw = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
    general_ledger = models.CharField(max_length=50)
    term_of_payment = models.CharField(max_length=50)
    note = models.CharField(max_length=50)
    newsletters = models.BooleanField(max_length=50)
