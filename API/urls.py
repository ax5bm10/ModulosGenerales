from django.conf.urls import url, include
from rest_framework import routers
from Clientes.views import ClienteViewSet


router = routers.DefaultRouter()
router.register('clientes',ClienteViewSet)

urlpatterns = [

    url(r'^',include(router.urls)),

]