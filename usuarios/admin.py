from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import CustomUser,EmpresaDB, Recomendacao

admin.site.register(CustomUser, auth_admin.UserAdmin)
admin.site.register(EmpresaDB)
admin.site.register(Recomendacao)

# Register your models here.
