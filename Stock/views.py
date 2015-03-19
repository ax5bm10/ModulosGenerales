from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from Stock.models import Productos
from Stock.serializers import ProductosSerializers


class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializers