# Generated by Django 3.0.14 on 2022-04-10 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0004_auto_20220326_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nhocustomfactsindicator',
            name='fact',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='nhocustomfactsindicator',
            name='icon',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='indicators.NHOCustomizationIcons', verbose_name='Font Icon'),
        ),
        migrations.AlterField(
            model_name='nhocustomfactsindicator',
            name='priority',
            field=models.SmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], verbose_name='Priority Level'),
        ),
    ]
