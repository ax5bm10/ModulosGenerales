from django.db import models

# Create your models here.

class Proveedores(models.Model):
    nombre = models.CharField(max_length=100)
    ruc = models.CharField(max_length=15)
    telefono = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    mail = models.CharField(max_length=100)
    fecha_agregacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s %s' % (self.nombre, self.ruc)

class UbicacionProveedores(models.Model):
    proveedor = models.ForeignKey(Proveedores)
    calle = models.CharField(max_length=100)
    nro = models.IntegerField()
    barrio = models.CharField(max_length=15)