from rest_framework import serializers
from Proveedores.models import  Proveedores, UbicacionProveedores


class ProveedoresSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Proveedores
        fields = ('nombre','ruc','telefono','celular','mail',)

class UbicacionProveedoresSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UbicacionProveedores
        fields = ('proveedor','calle','nro','barrio')