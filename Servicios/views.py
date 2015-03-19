from django.shortcuts import render
from rest_framework import viewsets
from Servicios.models import Servicio, Servicios
from Servicios.serializers import ServicioSerializer, ServiciosSerializer


class ServicioViewSet(viewsets.ModelViewSet):

    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class ServiciosViewSet(viewsets.ModelViewSet):

    queryset = Servicios.objects.all()
    serializer_class = ServiciosSerializer