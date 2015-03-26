from rest_framework import viewsets
from Clientes.models import Cliente, Ubicacion
from Clientes.serializers import ClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class UbicacionClienteViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = ClienteSerializer
