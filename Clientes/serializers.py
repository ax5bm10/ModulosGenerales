from rest_framework import serializers
from Clientes.models import Cliente, UbicacionCliente



class UbicacionClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = UbicacionCliente
        fields = ('calle','nro','barrio')



class ClienteSerializer(serializers.ModelSerializer):

    ubicaciones = UbicacionClienteSerializer(many=True,read_only=True)

    class Meta:
        model = Cliente
        fields = ('nombre','apellido','ci','ruc','telefono','celular','mail','ubicaciones',)


