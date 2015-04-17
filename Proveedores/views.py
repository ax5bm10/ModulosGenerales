from rest_framework import viewsets
from Proveedores.models import Proveedores, UbicacionProveedores
from Proveedores.serializers import ProveedoresSerializers, UbicacionProveedoresSerializer


class ProveedoresViewSet(viewsets.ModelViewSet):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializers

class UbicacionProveedoresViewSet(viewsets.ModelViewSet):
    queryset = UbicacionProveedores.objects.all()
    serializer_class = UbicacionProveedoresSerializer