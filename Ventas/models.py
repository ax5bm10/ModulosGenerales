from django.db import models

# Create your models here.
from Clientes.models import Cliente
from Stock.models import Productos


class Venta(models.Model):
    cliente = models.ForeignKey(Cliente)
    nro_comprobante = models.CharField(max_length=30)
    fecha_compra = models.DateTimeField()
    fecha_agregacion = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)

class Detalle_Venta(models.Model):
    venta = models.ForeignKey(Venta)
    producto = models.ForeignKey(Productos)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    descuento = models.IntegerField()