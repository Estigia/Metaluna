from django.conf.urls import url

from .views import (
                    agencia,
                    AgenciaDetail,
                    index,
                    AgenciaUpdate
                    )

urlpatterns = [

    url(r'^$', index, name='index'),
    url(r'^crear/', agencia, name='crear'),
    url(r'^(?P<pk>\d+)/detalles/', AgenciaDetail.as_view(),name='detalles'),
    url(r'^(?P<pk>\d+)/editar/', AgenciaUpdate.as_view(), name='editar'),


]
