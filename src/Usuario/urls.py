from django.conf.urls import url

from .views import (
            EmpleadoCreate,
            empleadoList,
            EmpleadoUpdate,
            EmpleadoDetail,
            usuarioList,
            )

urlpatterns = [
        url(r'^crear/', EmpleadoCreate.as_view(), name='empleadoCreate'),
        url(r'^$', empleadoList, name='empleadoList'),
        url(r'^(?P<pk>\d+)/editar', EmpleadoUpdate.as_view(), name='empleadoUpdate'),
        url(r'^(?P<pk>\d+)/detalles', EmpleadoDetail.as_view(), name='empleadoDetail'),
        url(r'^usuarios/$', usuarioList, name='usuarioList')
]
