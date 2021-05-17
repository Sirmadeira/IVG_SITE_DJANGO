from django.contrib import admin
from .models import DataDBC

admin.site.site_header= 'Admin data compras'


class DataDBAdmin(admin.ModelAdmin):
	list_display= ('marca','modelo','motor','ano','status','cor','localidade','combustivel','quilometragem','preco','autor','data_postada')
	list_filter= ('data_postada',)
admin.site.register(DataDBC, DataDBAdmin)
