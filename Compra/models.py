from django.db import models
from Proveedores.models import Proveedores
from Stock.models import Productos


# Create your models here.


class Compra(models.Model):
    proveedor = models.ForeignKey(Proveedores)
    nro_comprobante = models.CharField(max_length=30)
    fecha_compra = models.DateTimeField()
    fecha_agregacion = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)

class Detalle_Compra(models.Model):
    compra = models.ForeignKey(Compra)
    producto = models.ForeignKey(Productos)
    cantidad = models.IntegerField()
    precio_unitario = models.IntegerField(blank=True)
    precio_total = models.IntegerField(blank=True)