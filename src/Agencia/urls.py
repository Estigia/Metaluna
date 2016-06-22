from django.conf.urls import url

from .views import (
                    agencia,
                    AgenciaDetail,
                    index,
                    AgenciaUpdate,
                    VehiculoUpdate,
                    VehiculoDetail,
                    vehiculoList
                    )

urlpatterns = [

    url(r'^$', index, name='index'),
    url(r'^crear/', agencia, name='crear'),
    url(r'^(?P<pk>\d+)/detalles/', AgenciaDetail.as_view(),name='detalles'),
    url(r'^(?P<pk>\d+)/editar/', AgenciaUpdate.as_view(), name='editar'),
    url(r'^(?P<pk>\d+)/detalle_vehiculo',VehiculoDetail.as_view(), name='detail_v'),
    url(r'^(?P<pk>\d+)/editar_vehiculo',VehiculoUpdate.as_view(),name='edit_v'),
    url(r'^lista_vehiculo/',vehiculoList, name = 'list_v'),

]
