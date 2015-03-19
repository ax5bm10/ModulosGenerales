from rest_framework import viewsets
from Facturacion.models import Factura
from Facturacion.serializers import FacturaSerializers


class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializers