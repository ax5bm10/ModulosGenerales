from rest_framework import serializers
from Compra.models import Compra, Detalle_Compra
from Proveedores.serializers import ProveedoresSerializers
from Stock.serializers import ProductosSerializers


class DetalleCompraSerializer(serializers.ModelSerializer):

    producto = ProductosSerializers(many=False,read_only=True)

    class Meta:
        model = Detalle_Compra
        fields = ('producto','cantidad','precio_unitario','precio_total')


class CompraSerializer(serializers.ModelSerializer):

    proveedor = ProveedoresSerializers(many=False,read_only=True)
    detalles = DetalleCompraSerializer(many=True,read_only=True)

    class Meta:
        model = Compra
        fields = ('proveedor','nro_comprobante','fecha_compra','detalles',)