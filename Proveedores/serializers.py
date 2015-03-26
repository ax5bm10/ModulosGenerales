from rest_framework import serializers
from Clientes.models import Ubicacion
from Proveedores.models import  Proveedores, Ubicacion


class ProveedoresSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Proveedores
        fields = ('nombre','ruc','telefono','celular','mail',)

class UbicacionProveedoresSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ubicacion
        fields = ('proveedor','calle','nro','barrio')