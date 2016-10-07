from django.conf.urls import url

from .views import  (
                    index,
                    clientes,
                    ComodinCreate,
                    ProveedorDetail,
                    ProveedorUpdate,
                    ClienteDetail,
                    ClienteUpdate,
                    ClienteCreate
                    )


urlpatterns = [
    url(r'^proveedores/$', index, name='index'),
    url(r'^clientes/$', clientes, name='clientes'),
    url(r'^proveedores/crear/$',ComodinCreate.as_view(),name='comodinCreate'),
    url(r'^clientes/crear/$',ClienteCreate.as_view(),name='clientesCreate'),
    url(r'^proveedores/(?P<pk>\d+)/detallesProveedor/$', ProveedorDetail.as_view(),name='detallesProveedor'),
    url(r'^proveedores/(?P<pk>\d+)/editarProveedor/', ProveedorUpdate.as_view(), name='editarProveedor'),
    url(r'^clientes/(?P<pk>\d+)/detallesCliente/$', ClienteDetail.as_view(),name='detallesCliente'),
    url(r'^clientes/(?P<pk>\d+)/editarCliente/', ClienteUpdate.as_view(), name='editarCliente'),
]
