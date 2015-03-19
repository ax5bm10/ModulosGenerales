from rest_framework import serializers
from Servicios.models import Servicio, Servicios


class ServicioSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Servicio
        fields = ('cliente','factura','fecha_servicio')

class ServiciosSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Servicios
        fields = ('servicio','titulo','definicion','precio','descuento')