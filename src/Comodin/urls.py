from django.conf.urls import url

from .views import  (
                    index,
                    clientes,
                    ComodinCreate,
                    ProveedorDetail

                    )


urlpatterns = [
    url(r'^proveedores/', index, name='index'),
    url(r'^clientes/', clientes, name='clientes'),
    url(r'^crear/',ComodinCreate.as_view(),name='comodinCreate'),
    #-------Filtros de JS----------------------------

    url(r'^proveedores/detalles/$', ProveedorDetail.as_view(),name='detalles')
]
