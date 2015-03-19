from rest_framework import serializers
from Ventas.models import Venta, Detalle_Venta


class VentaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Venta
        fields = ('factura','cliente','fecha_venta')

class DetalleVentaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Detalle_Venta
        fields = ('venta','producto','cantidad','precio','descuento')