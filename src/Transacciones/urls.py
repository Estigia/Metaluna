from django.conf.urls import url

from .views import (
    ventas,
    compras,
    venta,
    compra,
    credito,
    facturaList,
    FacturaDetail
    )

urlpatterns = [
    url(r'^ventas/$',ventas, name='ventas'),
    url(r'^compras/$', compras, name='compras'),
    url(r'^venta/', venta, name='venta'),
    url(r'^compra/', compra, name='compra'),
    url(r'^compras/crear_credito', credito, name='compra_credito'),
    url(r'^ventas/crear_credito', credito, name='venta_credito'),
    url(r'^(compras)/facturas', facturaList, name='facturas_compras'),
    url(r'^(ventas)/facturas', facturaList, name='facturas_ventas'),
    url(r'^facturas/(?P<pk>\d+)/detalles', FacturaDetail.as_view(), name='facturas')
]
