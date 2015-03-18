from rest_framework import serializers
from Clientes.models import Cliente


class ClienteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cliente
        fields = ('nombre','apellido','ci','ruc','telefono','celular','mail',)