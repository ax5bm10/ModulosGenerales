from django.contrib import admin

# Register your models here.
from Ventas.models import Venta, Detalle_Venta

admin.site.register(Venta)
admin.site.register(Detalle_Venta)