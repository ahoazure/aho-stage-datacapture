from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DataQualityConfig(AppConfig):
    name = 'data_quality'
    verbose_name = _('Data Quality')
 
