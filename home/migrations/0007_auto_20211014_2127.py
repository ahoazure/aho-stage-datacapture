# Generated by Django 3.0.14 on 2021-10-14 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_stgperiodtype'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stgperiodtype',
            options={'managed': True, 'ordering': ('name',), 'verbose_name': 'Periodicity', 'verbose_name_plural': '   Periodicity Type'},
        ),
    ]
