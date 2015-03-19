from rest_framework import serializers
from Compra.models import Compra, Detalle_Compra

class CompraSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Compra
        fields = ('proveedor','nro_comprobante','fecha_compra')
        
class DetalleCompraSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Detalle_Compra
        fields = ('compra','producto','cantidad','precio_unitario','precio_total')