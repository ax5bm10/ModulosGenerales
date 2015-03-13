from django.db import models

# Create your models here.

class Productos(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=1000)
    cantidad = models.IntegerField()
    costo_unitario = models.IntegerField(null=True)
    costo_total = models.IntegerField(null=True)
