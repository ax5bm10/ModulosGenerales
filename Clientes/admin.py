from django.contrib import admin
from models import Cliente, Ubicacion
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','ruc')

class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('calle','nro','barrio')

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Ubicacion,UbicacionAdmin)