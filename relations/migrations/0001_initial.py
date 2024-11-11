# Generated by Django 5.0.6 on 2024-07-10 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_type', models.CharField(choices=[('company', 'Company'), ('relation', 'Relation')], max_length=50)),
                ('code', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('company_number', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('department', 'department')], max_length=50)),
                ('salutation', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=50)),
                ('postal', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
                ('quotation_mail', models.CharField(max_length=50)),
                ('reminders_mail', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('iban', models.CharField(max_length=50)),
                ('bic', models.CharField(max_length=50)),
                ('btw', models.CharField(max_length=50)),
                ('kind', models.CharField(max_length=50)),
                ('general_ledger', models.CharField(max_length=50)),
                ('term_of_payment', models.CharField(max_length=50)),
                ('note', models.CharField(max_length=50)),
                ('newsletters', models.BooleanField(max_length=50)),
            ],
        ),
    ]
