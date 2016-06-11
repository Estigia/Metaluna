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
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^calibre/', 'Producto.views.calibre', name='calibre'),
    url(r'^forma/', 'Producto.views.forma', name='forma'),
    url(r'^longitud/', 'Producto.views.longitud', name='longitud'),
    url(r'^lote/', 'Producto.views.lote', name='lote')
    url(r'^material/', 'Producto.views.material', name='material'),
    url(r'^productos/', 'Producto.views.productos', name='productos'),
    url(r'^tipo_producto/', 'Producto.views.tipo_producto', name='tipo_producto'),
]
