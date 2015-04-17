from rest_framework import serializers
from Clientes.serializers import ClienteSerializer
from Facturacion.serializers import FacturaSerializers
from Servicios.models import Servicio, DetalleServicio


class ServicioSerializer(serializers.ModelSerializer):

    cliente = ClienteSerializer(many=False,read_only=True)
    factura = FacturaSerializers(many=False,read_only=True)

    class Meta:
        model = Servicio
        fields = ('cliente','factura','fecha_servicio')

class DetalleServicioSerializer(serializers.HyperlinkedModelSerializer):



    class Meta:
        model = DetalleServicio
        fields = ('servicio','titulo','definicion','precio','descuento')