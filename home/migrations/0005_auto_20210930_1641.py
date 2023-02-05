# Generated by Django 3.0.14 on 2021-09-30 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_auto_20210929_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filesource',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User Name (Email)'),
        ),
    ]
