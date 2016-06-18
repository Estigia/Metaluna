from django.conf.urls import url

from .views import EmpleadoCreate

urlpatterns = [
        url(r'^crear/',EmpleadoCreate.as_view(),name='empleadoCreate')
]
