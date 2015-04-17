from django.db import models
from Clientes.models import Cliente
from Facturacion.models import Factura

# Create your models here.


class Servicio(models.Model):
    cliente = models.ForeignKey(Cliente)
    factura = models.ForeignKey(Factura)
    fecha_servicio = models.DateTimeField()
    fecha_agregacion = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)

class DetalleServicio(models.Model):
    servicio = models.ForeignKey(Servicio)
    titulo = models.CharField(max_length=100)
    definicion = models.TextField(max_length=1000)
    precio = models.IntegerField()
    descuento = models.IntegerField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
