from swampdragon.serializers.model_serializer import ModelSerializer

class ClienteSerializer(ModelSerializer):

    class Meta:
        model = 'Clientes.Cliente'