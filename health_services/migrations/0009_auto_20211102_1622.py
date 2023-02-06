# Generated by Django 3.0.14 on 2021-11-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_services', '0008_auto_20211102_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthservicesprogrammes',
            name='indicators',
            field=models.ManyToManyField(blank=True, db_table='stg_health_service_indicators', to='health_services.HealthServicesIndicators', verbose_name='HSC Indicators'),
        ),
        migrations.AlterField(
            model_name='healthservicesprogrammestranslation',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Programme Name'),
        ),
    ]