from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# pylint --load-plugins pylint_django 
# <path_to_your_sources>
# ImportExportModelAdmin

admin.site.site_header= 'Ecom Local Management'
class produit_admin(admin.ModelAdmin):
    list_filter=['date']
    list_display=['title'],['quantity'],['active']
    search_fields=['title'],['quantity']
# admin.site.register(Produits, produit_admin, ViewAdmin)

@admin.register(Product, Order )

class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )

