from django.conf.urls import url

from .views import ventas, compras, venta, compra, index

urlpatterns = [
    url(r'^ventas/',ventas, name='ventas'),
    url(r'^compras/', compras, name='compras'),
    url(r'^venta/', venta, name='venta'),
    url(r'^compra/', compra, name='compra'),
    url(r'^$', index, name='index')
]
