from django.conf.urls import url

from .views import (
    index,
    ProductoDetail,
    producto,
    lote,
    tipo_producto,
    calibre,
    forma,
    longitud,
    material
)

urlpatterns = [
    url(r'^$', index, name = 'index'),
    url(r'crear', producto, name = 'crear'),
    url(r'(?P<pk>\d+)',ProductoDetail.as_view(), name='detail'),
    url(r'crear_lote', lote, name = 'lote'),
    url(r'tipo_producto', tipo_producto, name = 'tipo_producto'),
    url(r'crear_forma', forma, name = 'forma'),
    url(r'crear_calibre', calibre, name = 'calibre'),
    url(r'crear_longitud', longitud, name = 'longitud'),
    url(r'crear_material', material, name = 'material'),
]
