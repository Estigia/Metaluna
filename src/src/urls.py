"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin

from Comodin.views import (
            ComodinCreate,
            MarcaCreate,
            ClienteCreate,
            filtroP
            )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^empleados/', include('Usuario.urls')),
    url(r'^inicio/','Usuario.views.inicio', name='login'),
    url(r'^registro/','Usuario.views.registro', name='registro'),
    url(r'^proveedor/',ComodinCreate.as_view(),name='proveedor'),
    url(r'^cliente/',ClienteCreate.as_view(), name = 'cliente'),
    url(r'^marca/',MarcaCreate.as_view(), name = 'marca'),
    url(r'^filtro/',filtroP,name = 'filtroP'),
    url(r'^calibre/', 'Producto.views.calibre', name='calibre'),
    url(r'^forma/', 'Producto.views.forma', name='forma'),
    url(r'^longitud/', 'Producto.views.longitud', name='longitud'),
    url(r'^lote/', 'Producto.views.lote', name='lote'),
    url(r'^material/', 'Producto.views.material', name='material'),
    url(r'^productos/', 'Producto.views.producto', name='productos'),
    url(r'^tipo_producto/', 'Producto.views.tipo_producto', name='tipo_producto'),
    url(r'^trans/','Transacciones.views.trans',name="trans"),
    url(r'^factura/','Transacciones.views.Factura', name="factura"),
    url(r'^detalleFactura/','Transacciones.views.DetalleFactura', name="detalleFactura"),
    url(r'^recibo/','Transacciones.views.Recibo', name="recibo"),
    url(r'^abonos/','Transacciones.views.Abonos', name="abonos"),
    url(r'^credito/','Transacciones.views.Credito', name="credito"),
    url(r'^agencia/', 'Agencia.views.Agencia', name='Agencia'),
    url(r'^vehiculo/', 'Agencia.views.Vehiculo', name='Vehiculo'),
    url(r'^entrega/', 'Agencia.views.Entrega', name='Entrega'),
    url(r'^mercaderia/', 'Agencia.views.Mercaderia', name='Mercaderia'),
    url(r'^planilla/', 'Planillas.views.Planilla', name='Planilla'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
