from rest_framework import serializers
from Proveedores.models import  Proveedores


class ProveedoresSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Proveedores
        fields = ('nombre','ruc','telefono','celular','mail',)