from django.db import models
from Clientes.models import Cliente

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length=100)
    definicion = models.TextField(max_length=1000)
    precio = models.IntegerField()
    descuento = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class Servicios(models.Model):
    cliente = models.ForeignKey(Cliente)
    servicio = models.ForeignKey(Servicio)