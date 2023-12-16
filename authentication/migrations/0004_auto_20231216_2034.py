# Generated by Django 3.0.14 on 2023-12-16 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0002_auto_20210916_1203'),
        ('authentication', '0003_auto_20210930_1641'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ahodctuserlogs',
            options={'managed': False, 'verbose_name': 'View Users Log', 'verbose_name_plural': ' View User Logs'},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='location',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='regions.StgLocation', verbose_name='Location Name'),
        ),
    ]
