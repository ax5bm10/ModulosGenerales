from django.shortcuts import render
from rest_framework import viewsets
from Proveedores.models import Proveedores
from Proveedores.serializers import ProveedoresSerializers


class ProveedoresViewSet(viewsets.ModelViewSet):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializers