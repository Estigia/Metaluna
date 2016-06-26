from django.conf.urls import url

from .views import facturacion

urlpatterns = [
    url(r'^facturacion/',facturacion, name='facturacion')
]
