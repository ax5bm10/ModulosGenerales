from rest_framework import serializers
from Clientes.models import Cliente, UbicacionCliente


class ClienteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cliente
        fields = ('nombre','apellido','ci','ruc','telefono','celular','mail',)


class UbicacionClienteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UbicacionCliente
        fields = ('cliente','calle','nro','barrio')