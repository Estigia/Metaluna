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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^trans/','Transacciones.views.trans',name="trans"),
    url(r'^factura/','Transacciones.views.Factura', name="factura"),
    url(r'^detalleFactura/','Transacciones.views.DetalleFactura', name="detalleFactura"),
    url(r'^recibo/','Transacciones.views.Recibo', name="recibo"),
    url(r'^abonos/','Transacciones.views.Abonos', name="abonos"),
    url(r'^credito/','Transacciones.views.Credito', name="credito"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
