# Generated by Django 3.0.14 on 2021-10-16 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_services', '0003_auto_20211015_0855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='healthservices_dataindicators',
            name='string_value',
        ),
        migrations.AddField(
            model_name='healthservices_dataindicators',
            name='value_calculated',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True, verbose_name='Calculated Value'),
        ),
    ]