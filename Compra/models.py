from django.db import models
from Proveedores.models import Proveedores
from Stock.models import Productos


# Create your models here.


class Compra(models.Model):
    proveedor = models.ForeignKey(Proveedores, related_name='proveedor')
    nro_comprobante = models.CharField(max_length=30)
    fecha_compra = models.DateTimeField()
    fecha_agregacion = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)

class Detalle_Compra(models.Model):
    compra = models.ForeignKey(Compra, related_name='detalles') #el related name es el encargado de decirle alserializer yo soy el que se esta colocando ahi
    producto = models.ForeignKey(Productos, related_name='producto')
    cantidad = models.IntegerField()
    precio_unitario = models.IntegerField(blank=True)
    precio_total = models.IntegerField(blank=True)