from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from Ventas.models import Venta, Detalle_Venta
from Ventas.serializers import VentaSerializer, DetalleVentaSerializer


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class DetalleVentaViewSet(viewsets.ModelViewSet):
    queryset = Detalle_Venta.objects.all()
    serializer_class = DetalleVentaSerializer
