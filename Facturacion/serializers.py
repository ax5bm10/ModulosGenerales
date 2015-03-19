from rest_framework import serializers
from Facturacion.models import Factura


class FacturaSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Factura
        fields = ('nro_factura','fecha_factura')