from rest_framework import viewsets
from Clientes.models import Cliente
from Clientes.serializers import ClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

