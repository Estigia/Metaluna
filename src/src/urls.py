"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from Comodin.views import (
            ComodinCreate,
            MarcaCreate,
            ClienteCreate,
            filtroP
            )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^empleados/', include('Usuario.urls')),
    url(r'^inicio/','Usuario.views.inicio', name='login'),
    url(r'^registro/','Usuario.views.registro', name='registro'),
    url(r'^proveedor/',ComodinCreate.as_view(),name='proveedor'),
    url(r'^cliente/',ClienteCreate.as_view(), name = 'cliente'),
    url(r'^marca/',MarcaCreate.as_view(), name = 'marca'),
    url(r'^filtro/',filtroP,name = 'filtroP'),
    ]
