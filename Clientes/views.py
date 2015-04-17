from rest_framework import viewsets
from Clientes.models import Cliente, UbicacionCliente
from Clientes.serializers import ClienteSerializer, UbicacionClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class UbicacionClienteViewSet(viewsets.ModelViewSet):
    queryset = UbicacionCliente.objects.all()
    serializer_class = UbicacionClienteSerializer
