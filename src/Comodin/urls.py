from django.conf.urls import url

from .views import  (
                    index,
                    clientes,
                    ComodinCreate

                    )


urlpatterns = [
    url(r'^proveedores/', index, name='index'),
    url(r'^clientes/', clientes, name='clientes'),
    url(r'^/crear/',ComodinCreate.as_view(),name='comodinCreate')
    #-------Filtros de JS----------------------------
]
