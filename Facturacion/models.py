from django.db import models

# Create your models here.

class Factura(models.Model):
    nro_factura = models.CharField(max_length=100)
    fecha_factura = models.DateTimeField()
    fecha_agregacion = models.DateTimeField(auto_now_add=True)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)