from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class actividades(models.Model):
    user_id = models.ForeignKey(User)
    actividad = models.CharField(max_length=10)
    fecha_hora = models.DateTimeField(auto_now=True)
    tabla_afectada = models.CharField(max_length=10)
    campo_afectado = models.IntegerField()