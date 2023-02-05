# Generated by Django 3.0.14 on 2021-09-16 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0002_auto_20210916_1203'),
        ('facilities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stgfacilityownership',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='regions.StgLocationCodes', verbose_name='Owner Country'),
        ),
        migrations.AlterField(
            model_name='stghealthfacility',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='regions.StgLocationCodes', verbose_name='Facility Country'),
        ),
    ]
