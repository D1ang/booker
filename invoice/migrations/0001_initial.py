# Generated by Django 5.0.6 on 2025-01-17 16:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('relations', '0002_relation_post_adress_relation_post_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_id', models.IntegerField()),
                ('invoice_date', models.DateField()),
                ('description', models.CharField(max_length=20, verbose_name='description')),
                ('payment_term', models.IntegerField()),
                ('latest_payment_date', models.DateField()),
                ('invoice_text', models.CharField(max_length=20, verbose_name='invoice text')),
                ('collect_invoice_amount', models.BooleanField()),
                ('invoice_to_bookkeeping', models.BooleanField()),
                ('mutation_description', models.CharField(max_length=20, verbose_name='mutation description')),
                ('send_invoice', models.BooleanField()),
                ('relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relations.relation')),
            ],
        ),
    ]
