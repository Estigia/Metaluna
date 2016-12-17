from django.conf.urls import url

from .views import (
                    agencia,
                    AgenciaDetail,
                    AgenciaEmpleadoList,
                    AgenciaProductoList,
                    index,
                    AgenciaUpdate,
                    VehiculoUpdate,
                    VehiculoDetail,
                    vehiculoList,
                    vehiculo,
                    EntregaUpdate,
                    entregaList,
                    EntregaDetail,
                    entrega,
                    mercaderia,
                    mercaderiaList,
                    MercaderiaDetail,
                    MercaderiaUpdate,
                    )

urlpatterns = [

    #------Agencias-------------------------------
    url(r'^$', index, name='index'),
    url(r'^crear/', agencia, name='crear'),
    url(r'^(?P<pk>\d+)/detalles/$', AgenciaDetail.as_view(),name='detalles'),
    url(r'^(?P<pk>\d+)/detalles/empleados', AgenciaEmpleadoList.as_view(),name='detalles_empleado'),
    url(r'^(?P<pk>\d+)/detalles/productos', AgenciaProductoList.as_view(),name='detalles_producto'),
    url(r'^(?P<pk>\d+)/editar/', AgenciaUpdate.as_view(), name='editar'),
    #------Vehiculos------------------------------
    url(r'^vehiculo/(?P<pk>\d+)/detalle/',VehiculoDetail.as_view(), name='detail_v'),
    url(r'^vehiculo/(?P<pk>\d+)/editar/',VehiculoUpdate.as_view(),name='edit_v'),
    url(r'^vehiculo/$',vehiculoList, name = 'list_v'),
    url(r'^vehiculo/crear/',vehiculo, name = 'crear_v'),
    #------Entregas-------------------------------
    url(r'^entrega/crear/',entrega,name = 'crear_e'),
    url(r'^entrega/(?P<pk>\d+)/detalle/', EntregaDetail.as_view(), name='detail_e'),
    url(r'^entrega/(?P<pk>\d+)/editar/', EntregaUpdate.as_view(), name='edit_e'),
    url(r'^entrega/vehiculo/(?P<vehiculo_id>\d+)', entregaList, name='list_e'),
    #------Mercaderia-----------------------------
    url(r'^mercaderia/crear/', mercaderia, name = 'crear_m'),
    url(r'^mercaderia/(?P<pk>\d+)/detalle/', MercaderiaDetail.as_view(), name='detail_m'),
    url(r'^mercaderia/(?P<pk>\d+)/editar/', MercaderiaUpdate.as_view(), name='edit_m'),
    url(r'^mercaderia/$', mercaderiaList, name='list_m'),

]
