from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class HealthServicesConfig(AppConfig):
    name = 'health_services'
    verbose_name = _('Health Services')
