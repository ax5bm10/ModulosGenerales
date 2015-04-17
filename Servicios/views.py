from rest_framework import viewsets
from Servicios.models import Servicio, DetalleServicio
from Servicios.serializers import ServicioSerializer,  DetalleServicioSerializer


class ServicioViewSet(viewsets.ModelViewSet):

    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class DetalleServicioViewSet(viewsets.ModelViewSet):

    queryset = DetalleServicio.objects.all()
    serializer_class = DetalleServicioSerializer