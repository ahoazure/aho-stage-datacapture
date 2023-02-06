from admin_auto_filters.filters import AutocompleteFilter
from django.shortcuts import reverse

class LocationFilter(AutocompleteFilter):
    title = 'Country or Region Name' # display title eg By Country or Region Name
    field_name = 'location' # name of the foreign key field from child model

    def get_autocomplete_url(self, request, model_admin):
        return reverse('admin:location_search')


class IndicatorsFilter(AutocompleteFilter):
    title = 'Indicator Name' # display title eg By Country or Region Name
    field_name = 'indicator' # name of the foreign key field from child model

    def get_autocomplete_url(self, request, model_admin):
        return reverse('admin:indicator_search')


class DatasourceFilter(AutocompleteFilter):
    title = 'Data Source Name' # display title eg By Country or Region Name
    field_name = 'datasource' # name of the foreign key field from child model

    def get_autocomplete_url(self, request, model_admin):
        return reverse('admin:source_search')


class CategoryOptionFilter(AutocompleteFilter):
    title = 'Disaggregation Option' # display title eg By Country or Region Name
    field_name = 'categoryoption' # name of the foreign key field from child model
    
    def get_autocomplete_url(self, request, model_admin):
        return reverse('admin:categories_search')
    

class KnowledgeResourceFilter(AutocompleteFilter):
    title = 'Knowledge Resource Types' # display title eg By Country or Region Name
    field_name = 'type' # name of the foreign key field from child model
    
    def get_autocomplete_url(self, request, model_admin):
        return reverse('admin:products_search')
    

class HealthCadreFilter(AutocompleteFilter):
    title = 'Type of Occupation' # display title eg By Country or Region Name
    field_name = 'cadre' # name of the foreign key field from child model
    
    def get_autocomplete_url(self, request, model_admin):
        return reverse('admin:cadre_search')