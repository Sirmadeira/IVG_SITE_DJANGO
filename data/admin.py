from django.contrib import admin
from .models import DataDB


admin.site.site_header= 'Admin data vendas'

class DataDBAdmin(admin.ModelAdmin):
	list_display= ('marca','modelo','motor','ano','status','cor','localidade','combustivel','quilometragem','preco','lucro','autor','data_postada')
	list_filter= ('data_postada',)

admin.site.register(DataDB,DataDBAdmin)
