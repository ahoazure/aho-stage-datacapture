
from django.contrib import admin
from django.contrib.admin import AdminSite #customize adminsite
#these libraries are imported to support monkey of admin_menu package
from django.urls import resolve, reverse, NoReverseMatch
from django.utils.text import capfirst
#import custom menu for customization to change apps order
from admin_menu.templatetags import custom_admin_menu
from import_export.admin import (ImportExportModelAdmin, ExportActionModelAdmin,
    ExportMixin,ImportMixin,ExportActionModelAdmin,ImportExportActionModelAdmin) #added exportaction mixin only
from import_export.formats import base_formats
from django.utils.translation import ugettext_lazy as _
# Customize the site admin header for login, title bar, and data admin form section.
class AdminSite(AdminSite):
    site_header = 'African Health Observatory' #also shown on login form
    site_title = 'AHO Data Capture and Admin Tool' #shown on the title bar
    index_title = 'African Health Observatory Data Management' #shown in the content section

# #Import this method and do nothing to it. It is required by get_app_list()!!
def get_admin_site(context):
    pass

get_admin_site = custom_admin_menu.get_admin_site #assign as is!

# Now this is the method that does the menu tweaks using the ordering dict!!!
def get_app_list(context, order=True):
    admin_site = get_admin_site(context)
    request = context['request']

    # import pdb; pdb.set_trace()


    app_dict = {}
    for model, model_admin in admin_site._registry.items():
        app_label = model._meta.app_label
        try:
            has_module_perms = model_admin.has_module_permission(request)
        except AttributeError:
            has_module_perms = request.user.has_module_perms(app_label)

        if has_module_perms:
            perms = model_admin.get_model_perms(request)

            # Check whether user has any perm for this model.
            # If so, add the model to the model_dict.
            if True in perms.values():
                info = (app_label, model._meta.model_name)
                model_dict = {
                    'name': capfirst(model._meta.verbose_name_plural),
                    'object_name': model._meta.object_name,
                    'perms': perms,
                    'model_admin': model_admin,
                }
                if perms.get('change', False):
                    try:
                        model_dict['admin_url'] = reverse(
                        'admin:%s_%s_changelist'%info,current_app=admin_site.name)
                    except NoReverseMatch:
                        pass
                if perms.get('add', False):
                    try:
                        model_dict['add_url'] = reverse(
                        'admin:%s_%s_add' % info, current_app=admin_site.name)
                    except NoReverseMatch:
                        pass
                if app_label in app_dict:
                    app_dict[app_label]['models'].append(model_dict)
                else:
                    try:
                        name = apps.get_app_config(app_label).verbose_name
                    except NameError:
                        if app_label.title().upper() == 'UHC_CLOCK':
                            name =_("UHC CLOCK") # rename the horizontal menu; added on 02/01/2024
                        elif app_label.title().upper() == 'AUTHTOKEN':
                            name =_("API TOKENS") # rename the horizontal menu; added on 02/01/2024
                        elif app_label.title().upper() == 'HEALTH_WORKFORCE':
                            name =_("HEALTH WORKFORCE") # rename the horizontal menu; added on 02/01/2024
                        elif app_label.title().upper() == 'HEALTH_SERVICES':
                            name =_("HEALTH SERVICES") # rename the horizontal menu; added on 02/01/2024
                        elif app_label.title().upper() == 'ELEMENTS':
                            name =_("DATA ELEMENTS") # rename the horizontal menu; added on 02/01/2024
                        elif app_label.title().upper() == 'DATA_WIZARD':
                            name =_("DATA WIZARD") # rename the horizontal menu; added on 02/01/2024
                        elif app_label.title().upper() == 'DATA_QUALITY':
                            name =_("DATA QUALITY") # rename the horizontal menu; added on 02/01/2024
                        else:
                             name = _(app_label.title().upper()) # convert default app label to uppercase
                    
                    app_dict[app_label] = {
                        'name': name,
                        'app_label': app_label,
                        'app_url': reverse(
                            'admin:app_list',
                            kwargs={'app_label': app_label},
                            current_app=admin_site.name,
                        ),
                        'has_module_perms': has_module_perms,
                        'models': [model_dict],
                    }

    # This dict has been added to take care of modules ordering on the interface
    ordering = {
    'Home':1,
    'Indicators':2,
    'Publications':3,
    'Facilities':4,
    'Health Workforce':5, # Health_Workforce
    'Health Services':6, # Health_Services
    'Data Elements':7, # Elements
    'Regions':8,
    'Data Wizard':9, # Data_Wizard
    'Data Quality':10, # Data_Quality
    'api tokens':11, # Authtoken
    'Authentication':12,
    'UHC Clock':13,
    }

    ordering =  {k.upper(): v for k, v in ordering.items()}
         
    # Create the list to be sorted using the ordering dict.
    app_list = list(app_dict.values())
    
    # import pdb; pdb.set_trace()

    
    if order:
        app_list.sort(key=lambda x: ordering[x['name']])
        # Sort the models alphabetically within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: x['name'])
    
    # import pdb; pdb.set_trace()

    return app_list
  
# apply custom menu converted to uppercase
custom_admin_menu.get_app_list = get_app_list


class OverideImportExport(ImportExportModelAdmin):
    def get_import_formats(self):
        # Returns available import/export formats.
        formats = (
              base_formats.CSV,
              base_formats.XLS,
              base_formats.XLSX,
        )
        return [f for f in formats if f().can_import()]

    def get_export_formats(self):
        # Returns available import/export formats.
        formats = (
              base_formats.CSV,
              base_formats.XLS,
              base_formats.XLSX,
        )
        return [f for f in formats if f().can_export()]

# Used to override export base format types to limit to only CSV,XLS and XLSx
class OverideExport(ExportMixin, admin.ModelAdmin):
    def get_export_formats(self):
        # Returns available export formats.
        formats = (
              base_formats.CSV,
              base_formats.XLS,
              base_formats.XLSX,
        )
        return [f for f in formats if f().can_export()]


# Used override export base format types to limit to only CSV,XLS and XLSx
class OverideExportAdmin(ExportActionModelAdmin, ExportMixin, admin.ModelAdmin):
    def get_export_formats(self):
        # Returns available export formats.
        formats = (
              base_formats.CSV,
              base_formats.XLS,
              base_formats.XLSX,
        )
        return [f for f in formats if f().can_export()]

# Used to override import base format types to limit to only CSV,XLS and XLSx
class OverideImport(ImportMixin, admin.ModelAdmin):
    def get_import_formats(self):
        # Returns available import formats.
        formats = (
              base_formats.CSV,
              base_formats.XLS,
              base_formats.XLSX,
        )
        return [f for f in formats if f().can_import()]
