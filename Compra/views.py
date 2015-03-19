from rest_framework import viewsets
from Compra.models import Compra
from Compra.models import Detalle_Compra
from Compra.serializers import CompraSerializer, DetalleCompraSerializer


class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

class DetalleCompraViewSet(viewsets.ModelViewSet):
    queryset = Detalle_Compra.objects.all()
    serializer_class = DetalleCompraSerializer