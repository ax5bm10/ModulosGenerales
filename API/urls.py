from django.conf.urls import url, include
from rest_framework import routers
from Clientes.views import ClienteViewSet
from Proveedores.views import ProveedoresViewSet


router = routers.DefaultRouter()
router.register('clientes',ClienteViewSet)
router.register('proveedores',ProveedoresViewSet)

urlpatterns = [

    url(r'^',include(router.urls)),

]