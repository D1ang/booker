# Generated by Django 4.2.11 on 2024-12-04 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0002_relation_post_adress_relation_post_city_and_more'),
        ('quotation', '0002_progresstypes'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='relation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='relations.relation'),
            preserve_default=False,
        ),
    ]
