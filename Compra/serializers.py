from rest_framework import serializers
from Compra.models import Compra, Detalle_Compra


class DetalleCompraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Detalle_Compra
        fields = ('producto','cantidad','precio_unitario','precio_total')


class CompraSerializer(serializers.ModelSerializer):

    detalles = DetalleCompraSerializer(many=True,read_only=True)

    class Meta:
        model = Compra
        fields = ('proveedor','nro_comprobante','fecha_compra','detalles',)