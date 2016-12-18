from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.core.serializers.json import Serializer
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import (Lote, Producto, Tipo_Producto,
                        Material, Longitud, Calibre, Forma)
from Comodin.models import Marca
from Agencia.models import Mercaderia
from .forms import (LoteForm, ProductoForm, Tipo_ProductoForm,
                    MaterialForm, LongitudForm, CalibreForm, FormaForm)

#Vistas de Producto y Detalle -----------------------------
@login_required(login_url='base')
def index(request):
    productos = Producto.objects.all()

    if request.GET:
        try:
            productos = productos.filter(descripcion__icontains=request.GET['descripcion'])
        except:
            pass
        try:
            productos = productos.filter(Tipo_Producto_id__id=request.GET['tipo'])
        except:
            pass
        try:
            productos = productos.filter(Material_id__id=request.GET['material'])
        except:
            pass
        try:
            productos = productos.filter(Longitud_id=request.GET['longitud'])
        except:
            pass
        try:
            productos = productos.filter(Calibre_id__id=request.GET['calibre'])
        except:
            pass
        try:
            productos = productos.filter(Forma_id__id=request.GET['forma'])
        except:
            pass
        try:
            productos = productos.filter(Marca_id__id=request.GET['marca'])
        except:
            pass

    context = {
        "productos" : productos,
        "tipos": Tipo_Producto.objects.all(),
        "materiales": Material.objects.all(),
        "longitudes": Longitud.objects.all(),
        "calibres": Calibre.objects.all(),
        "formas": Forma.objects.all(),
        "marcas": Marca.objects.all()
    }

    return render(request, 'producto/producto_list.html', context)

class ProductoDetail(DetailView):
    model = Producto
    template_name = 'producto/producto_detail.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProductoDetail, self).dispatch(request, *args, **kwargs)

class ProductoUpdate(UpdateView):
    if not request.user.is_staff:
        return HttpResponseRedirect('/')

    model = Producto
    template_name = 'producto/producto_edit.html'
    success_url = reverse_lazy('Producto:index')
    fields = [
        "descripcion" ,
        "Tipo_Producto_id",
        "Material_id",
        "Longitud_id",
        "Calibre_id",
        "Forma_id",
        "Marca_id"
    ]

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProductoUpdate, self).dispatch(request, *args, **kwargs)

@login_required(login_url='base')
def producto(request):
    if not request.user.is_staff:
        return HttpResponseRedirect('/')

    form = ProductoForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        form.save()
        return redirect('Producto:index')

    return render(request, 'producto/productos.html', context)

#--------------------------------------------------------
@login_required(login_url='base')
def lote(request):
    if not request.user.is_staff:
        return HttpResponseRedirect('/')

    form = LoteForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        form.save()

    return render(request, 'producto/lote.html', context)

@login_required(login_url='base')
def tipo_producto(request):
    if not request.user.is_staff:
        return HttpResponseRedirect('/')

    form = Tipo_ProductoForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        form.save()

    return render(request, 'producto/tipo_producto.html', context)

@login_required(login_url='base')
def material(request):
    if not request.user.is_staff:
        return HttpResponseRedirect('/')

    form = MaterialForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        form.save()

    return render(request, 'producto/material.html', context)

@login_required(login_url='base')
def longitud(request):
    if not request.user.is_staff:
        return HttpResponseRedirect('/')

    form = LongitudForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        form.save()

    return render(request, 'producto/longitud.html', context)

@login_required(login_url='base')
def calibre(request):
    if not request.user.is_staff:
        return HttpResponseRedirect('/')

    form = CalibreForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        form.save()

    return render(request, 'producto/calibre.html', context)

@login_required(login_url='base')
def forma(request):
    if not request.user.is_staff:
        return HttpResponseRedirect('/')

    form = FormaForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        form.save()

    return render(request, 'producto/forma.html', context)


#Serializador de filtroProducto--------------------------------

# class ProductoSerializer(Serializer):
#
#     def get_dump_object(self, obj):
#         dic = super(ProductoSerializer, self).get_dump_object(obj)

#--------------------------------------------------------------

@login_required(login_url='base')
def existencias(request):
    id_producto = request.GET['producto']
    agencia = request.user.Empleado_id.Agencia_id

    existencias = Mercaderia.objects.filter(
        Producto_id__id = id_producto,
        Agencia_id = agencia
    )

    data = serializers.serialize('json', existencias, fields=('cantidad'))

    if not len(existencias):
        return HttpResponseBadRequest()

    return HttpResponse(data, content_type='application/json')

@login_required(login_url='base')
def filtroProducto(request):
    id_marca = request.GET['id_marca']
    id_tipo = request.GET['id_tipo']

    productos = Producto.objects.filter(
                    Marca_id= id_marca,
                    Tipo_Producto_id= id_tipo
                    )

    data = serializers.serialize('json', productos, indent=2, use_natural_foreign_keys=True, use_natural_primary_keys=True)

    return HttpResponse(data, content_type='application/json')
