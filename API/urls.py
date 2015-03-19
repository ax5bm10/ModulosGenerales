from django.conf.urls import url, include
from rest_framework import routers
from Clientes.views import ClienteViewSet
from Compra.views import CompraViewSet, DetalleCompraViewSet
from Proveedores.views import ProveedoresViewSet
from Servicios.views import ServicioViewSet, ServiciosViewSet
from Stock.views import ProductosViewSet


router = routers.DefaultRouter()
router.register('clientes',ClienteViewSet)

router.register('proveedores',ProveedoresViewSet)

router.register('compra',CompraViewSet)
router.register('detalle-compra',DetalleCompraViewSet)

router.register('servicio',ServicioViewSet)
router.register('servicios',ServiciosViewSet)

router.register('productos',ProductosViewSet)


urlpatterns = [

    url(r'^',include(router.urls)),

]