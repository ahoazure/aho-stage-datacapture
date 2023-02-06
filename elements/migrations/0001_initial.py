# Generated by Django 3.0.14 on 2021-08-26 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('regions', '0001_initial'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StgDataElement',
            fields=[
                ('dataelement_id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(default=uuid.uuid4, editable=False, max_length=36, unique=True, verbose_name='Unique ID')),
                ('code', models.CharField(blank=True, max_length=45, unique=True)),
                ('aggregation_type', models.CharField(choices=[('Count', 'Count'), ('Sum', 'Sum'), ('Average', 'Average'), ('Standard Deviation', 'Standard Deviation'), ('Variance', 'Variance'), ('Min', 'Min'), ('max', 'max'), ('None', 'None')], default='Count', max_length=45, verbose_name='Aggregate Type')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created')),
                ('date_lastupdated', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Modified')),
            ],
            options={
                'verbose_name': 'Element',
                'verbose_name_plural': 'Data Elements',
                'db_table': 'stg_data_element',
                'ordering': ('translations__name',),
                'managed': True,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StgDataElementGroup',
            fields=[
                ('group_id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(default=uuid.uuid4, editable=False, max_length=36, unique=True, verbose_name='Unique ID')),
                ('code', models.CharField(blank=True, max_length=50, unique=True, verbose_name='Group Code')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created')),
                ('date_lastupdated', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Modified')),
                ('dataelement', models.ManyToManyField(blank=True, db_table='stg_data_element_membership', to='elements.StgDataElement', verbose_name='Data Elements')),
            ],
            options={
                'verbose_name': 'Element Group',
                'verbose_name_plural': 'Element Groups',
                'db_table': 'stg_data_element_group',
                'ordering': ('translations__name',),
                'managed': True,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='DataElementProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Multi_Records Form',
                'verbose_name_plural': '  Multi_Records Form',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('elements.stgdataelement',),
        ),
        migrations.CreateModel(
            name='StgDataElementTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=230, verbose_name='Data Element Name')),
                ('shortname', models.CharField(max_length=50, verbose_name='short name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='elements.StgDataElement')),
            ],
            options={
                'verbose_name': 'Element Translation',
                'db_table': 'stg_data_element_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StgDataElementGroupTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=200, verbose_name='Group Name')),
                ('shortname', models.CharField(max_length=120, unique=True, verbose_name='Short Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='elements.StgDataElementGroup')),
            ],
            options={
                'verbose_name': 'Element Group Translation',
                'db_table': 'stg_data_element_group_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='FactDataElement',
            fields=[
                ('fact_id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(default=uuid.uuid4, editable=False, max_length=36, unique=True, verbose_name='Unique ID')),
                ('value', models.DecimalField(decimal_places=3, max_digits=20, verbose_name='Data Value')),
                ('target_value', models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True, verbose_name='Target Value')),
                ('start_year', models.IntegerField(default=2021, verbose_name='Start Year')),
                ('end_year', models.IntegerField(default=2021, verbose_name='Ending Year')),
                ('period', models.CharField(blank=True, max_length=10, verbose_name='Period')),
                ('comment', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10, verbose_name='Status')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created')),
                ('date_lastupdated', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Modified')),
                ('categoryoption', models.ForeignKey(default=999, on_delete=django.db.models.deletion.PROTECT, to='home.StgCategoryoption', verbose_name='Disaggregation Option')),
                ('dataelement', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='elements.StgDataElement', verbose_name='Data Element')),
                ('datasource', models.ForeignKey(default=4, on_delete=django.db.models.deletion.PROTECT, to='home.StgDatasource', verbose_name='Data Source')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='regions.StgLocation', verbose_name='Location')),
                ('user', models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User Name (Email)')),
                ('valuetype', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='home.StgValueDatatype', verbose_name='Data Type')),
            ],
            options={
                'verbose_name': 'Data Element',
                'verbose_name_plural': '   Single-Record Form',
                'db_table': 'fact_data_element',
                'ordering': ('location',),
                'permissions': (('approve_factdataelement', 'Can approve Data Element'), ('reject_factdataelement', 'Can reject Data Element'), ('pend_factdataelement', 'Can pend Data Element')),
                'managed': True,
                'unique_together': {('dataelement', 'location', 'datasource', 'categoryoption', 'start_year', 'end_year')},
            },
        ),
    ]