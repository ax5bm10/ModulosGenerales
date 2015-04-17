from django.contrib import admin
from models import Cliente, UbicacionCliente
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','ruc')

class UbicacionClienteAdmin(admin.ModelAdmin):
    list_display = ('calle','nro','barrio')

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(UbicacionCliente,UbicacionClienteAdmin)