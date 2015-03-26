from rest_framework import serializers
from Clientes.models import Cliente, Ubicacion


class ClienteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cliente
        fields = ('nombre','apellido','ci','ruc','telefono','celular','mail',)


class UbicacionClienteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ubicacion
        fields = ('cliente','calle','nro','barrio')