# Generated by Django 3.0.14 on 2021-09-04 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0004_auto_20210830_1734'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stgknowledgeproducttranslation',
            unique_together={('language_code', 'title', 'year_published', 'author'), ('language_code', 'master')},
        ),
    ]