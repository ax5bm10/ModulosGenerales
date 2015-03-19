from rest_framework import serializers
from Stock.models import Productos


class ProductosSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Productos
        fields = ('codigo','nombre','descripcion','cantidad','costo_unitario','costo_total')