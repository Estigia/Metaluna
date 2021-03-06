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
    #Esta es la url de admin.
    url(r'^880e0d76/', admin.site.urls),
    url(r'^empleados/', include('Usuario.urls', namespace='Usuario')),
    url(r'^agencia/', include('Agencia.urls', namespace='Agencia')),
    url(r'^transacciones/', include('Transacciones.urls', namespace='Transacciones')),
    url(r'^registro/','Usuario.views.registro', name='registro'),
    url(r'^empresa/',include('Comodin.urls', namespace='index')),
    url(r'^finanzas/','Planillas.views.finanzas', name= 'finanzas'),
    # url(r'^clientes/$','Comodin.views.clientes', name='clientes'),
    url(r'^marca/',MarcaCreate.as_view(), name = 'marca'),
    url(r'^filtro/',filtroP,name = 'filtroP'),
    url(r'^productos/', include('Producto.urls', namespace= 'Producto')),
    url(r'^trans/','Transacciones.views.trans',name="trans"),
    url(r'^$','Usuario.views.inicio',name="base"),
    url(r'^logout/$', 'Usuario.views.cerrar', name='cerrar'),
    url(r'^filtro_m/$', 'Localizaciones.views.BusquedaMunicipio', name='filtro_municipio')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
else:
    urlpatterns += url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.STATIC_ROOT}),
