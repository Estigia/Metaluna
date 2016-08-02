from django.conf.urls import url

from .views import  (
                    index,
                    clientes,
                    ComodinCreate,
                    ProveedorDetail,
                    ProveedorUpdate,
                    ClienteDetail,
                    ClienteUpdate,

                    )


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'clientes/', clientes, name='clientes'),
    url(r'^crear/',ComodinCreate.as_view(),name='comodinCreate'),
    url(r'^(?P<pk>\d+)/detallesProveedor/$', ProveedorDetail.as_view(),name='detallesProveedor'),
    url(r'^(?P<pk>\d+)/editarProveedor/', ProveedorUpdate.as_view(), name='editarProveedor'),
    url(r'^(?P<pk>\d+)/detallesCliente/$', ClienteDetail.as_view(),name='detallesCliente'),
    url(r'^(?P<pk>\d+)/editarCliente/', ClienteUpdate.as_view(), name='editarCliente'),
]
