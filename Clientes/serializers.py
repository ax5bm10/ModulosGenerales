from rest_framework import serializers

class ClienteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = 'Clientes.Cliente'
        fields = ('nombre','apellido','ci','ruc','telefono','celular','mail',)