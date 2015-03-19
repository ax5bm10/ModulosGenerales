from django.conf.urls import url, include
from rest_framework import routers
from Clientes.views import ClienteViewSet
from Compra.views import CompraViewSet, DetalleCompraViewSet
from Proveedores.views import ProveedoresViewSet


router = routers.DefaultRouter()
router.register('clientes',ClienteViewSet)

router.register('proveedores',ProveedoresViewSet)

router.register('compra',CompraViewSet)
router.register('detalle-compra',DetalleCompraViewSet)


urlpatterns = [

    url(r'^',include(router.urls)),

]