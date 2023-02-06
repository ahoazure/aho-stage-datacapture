# Generated by Django 3.0.14 on 2021-08-26 06:38

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StgEconomicZones',
            fields=[
                ('economiczone_id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(default=uuid.uuid4, editable=False, max_length=36, unique=True, verbose_name='Unique ID')),
                ('code', models.CharField(blank=True, max_length=50, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created')),
                ('date_lastupdated', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Modified')),
            ],
            options={
                'verbose_name': 'Economic Block',
                'verbose_name_plural': 'Economic Blocks',
                'db_table': 'stg_economic_zones',
                'ordering': ('translations__name',),
                'managed': True,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StgLocation',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(default=uuid.uuid4, editable=False, max_length=36, unique=True, verbose_name='Unique ID')),
                ('iso_alpha', models.CharField(max_length=15, unique=True, verbose_name='ISO Alpha Code')),
                ('iso_number', models.CharField(max_length=15, unique=True, verbose_name='ISO Numeric Code')),
                ('code', models.CharField(blank=True, max_length=15, unique=True, verbose_name='Unique Code')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created')),
                ('date_lastupdated', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Modified')),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': '   Locations',
                'db_table': 'stg_location',
                'ordering': ('translations__name',),
                'managed': True,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StgLocationLevel',
            fields=[
                ('locationlevel_id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(default=uuid.uuid4, editable=False, max_length=36, unique=True, verbose_name='Unique ID')),
                ('code', models.CharField(blank=True, max_length=50, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created')),
                ('date_lastupdated', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Modified')),
            ],
            options={
                'verbose_name': 'Location Level',
                'verbose_name_plural': '  Location Levels',
                'db_table': 'stg_location_level',
                'ordering': ('translations__name',),
                'managed': True,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StgSpecialcategorization',
            fields=[
                ('specialstates_id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(default=uuid.uuid4, editable=False, max_length=36, unique=True, verbose_name='Unique ID')),
                ('code', models.CharField(blank=True, max_length=50, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created')),
                ('date_lastupdated', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Modified')),
            ],
            options={
                'verbose_name': 'Categorization',
                'verbose_name_plural': 'Special Categorizations',
                'db_table': 'stg_specialcategorization',
                'ordering': ('translations__name',),
                'managed': True,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StgWorldbankIncomegroups',
            fields=[
                ('wb_income_groupid', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(default=uuid.uuid4, editable=False, max_length=36, unique=True, verbose_name='Unique ID')),
                ('code', models.CharField(blank=True, max_length=50, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created')),
                ('date_lastupdated', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Modified')),
            ],
            options={
                'verbose_name': 'Income Group',
                'verbose_name_plural': 'Income Groups',
                'db_table': 'stg_worldbank_incomegroups',
                'ordering': ('translations__name',),
                'managed': True,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StgLocationCodes',
            fields=[
                ('location', models.OneToOneField(help_text='You are not allowed to make changes to this Field because it             is related to countries already registed', on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='regions.StgLocation', verbose_name='Country')),
                ('country_code', models.CharField(max_length=15, unique=True, verbose_name='Dial Code')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created')),
                ('date_lastupdated', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Modified')),
            ],
            options={
                'verbose_name': 'Dial Code',
                'verbose_name_plural': 'Dial Codes',
                'db_table': 'stg_location_codes',
                'ordering': ('location',),
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='stglocation',
            name='locationlevel',
            field=models.ForeignKey(help_text='You are not allowed to make changes to this Field because it             is related to other Records', on_delete=django.db.models.deletion.PROTECT, to='regions.StgLocationLevel', verbose_name='Location Level'),
        ),
        migrations.AddField(
            model_name='stglocation',
            name='parent',
            field=models.ForeignKey(blank=True, default=1, help_text='You are not allowed to edit this field because it is        related to other records', null=True, on_delete=django.db.models.deletion.PROTECT, to='regions.StgLocation', verbose_name='Parent Location'),
        ),
        migrations.AddField(
            model_name='stglocation',
            name='special',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='regions.StgSpecialcategorization', verbose_name='Special Categorization'),
        ),
        migrations.AddField(
            model_name='stglocation',
            name='wb_income',
            field=models.ForeignKey(default='99', on_delete=django.db.models.deletion.PROTECT, to='regions.StgWorldbankIncomegroups', verbose_name='Income level'),
        ),
        migrations.AddField(
            model_name='stglocation',
            name='zone',
            field=models.ManyToManyField(blank=True, db_table='stg_economic_group_members', to='regions.StgEconomicZones', verbose_name='Economic Block'),
        ),
        migrations.CreateModel(
            name='StgWorldbankIncomegroupsTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=230, verbose_name='Income level')),
                ('shortname', models.CharField(max_length=50, unique=True, verbose_name='Short Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Brief Description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='regions.StgWorldbankIncomegroups')),
            ],
            options={
                'verbose_name': 'Income Group Translation',
                'db_table': 'stg_worldbank_incomegroups_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StgSpecialcategorizationTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=230, verbose_name='Categorization Name')),
                ('shortname', models.CharField(max_length=50, unique=True, verbose_name='Short Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Brief Description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='regions.StgSpecialcategorization')),
            ],
            options={
                'verbose_name': 'Categorization Translation',
                'db_table': 'stg_specialcategorization_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StgLocationTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=230, verbose_name='Location Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Brief Description')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Latitude')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Longitude')),
                ('cordinate', models.TextField(blank=True, null=True, verbose_name='Cordinates')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='regions.StgLocation')),
            ],
            options={
                'verbose_name': 'Location Translation',
                'db_table': 'stg_location_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StgLocationLevelTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('type', models.CharField(choices=[('level 1', 'level 1'), ('Level 2', 'Level 2'), ('Level 3', 'Level 3'), ('Level 4', 'Level 4'), ('Level 5', 'Level 5'), ('Level 6', 'Level 6'), ('Level 7', 'Level 7')], default='level 1', max_length=50, verbose_name='Location Level')),
                ('name', models.CharField(max_length=230, verbose_name='Level Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='regions.StgLocationLevel')),
            ],
            options={
                'verbose_name': 'Location Level Translation',
                'db_table': 'stg_location_level_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StgEconomicZonesTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=230, verbose_name='Economic Zone')),
                ('shortname', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Short Name')),
                ('description', models.TextField(blank=True, null=True)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='regions.StgEconomicZones')),
            ],
            options={
                'verbose_name': 'Economic Block Translation',
                'db_table': 'stg_economic_zones_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]