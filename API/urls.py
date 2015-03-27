from django.conf.urls import url, include
from rest_framework import routers
from Clientes.views import ClienteViewSet, UbicacionClienteViewSet
from Compra.views import CompraViewSet, DetalleCompraViewSet
from Facturacion.views import FacturaViewSet
from Proveedores.views import ProveedoresViewSet, UbicacionProveedoresViewSet
from Servicios.views import ServicioViewSet, ServiciosViewSet
from Stock.views import ProductosViewSet
from Ventas.views import VentaViewSet, DetalleVentaViewSet


router = routers.DefaultRouter()
router.register('clientes',ClienteViewSet)
router.register('ubicacion-cliente',UbicacionClienteViewSet)

router.register('proveedores',ProveedoresViewSet)
router.register('ubicacion-proveedores',UbicacionProveedoresViewSet)

router.register('detalle-compra',DetalleCompraViewSet)
router.register('compra',CompraViewSet)

router.register('servicio',ServicioViewSet)
router.register('servicios',ServiciosViewSet)

router.register('productos',ProductosViewSet)

router.register('ventas',VentaViewSet)
router.register('detalle-venta',DetalleVentaViewSet)

router.register('factura',FacturaViewSet)

urlpatterns = [

    url(r'^',include(router.urls)),

]