from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse
from django.core import serializers

from .models import (Lote, Producto, Tipo_Producto,
                        Material, Longitud, Calibre, Forma)
from .forms import (LoteForm, ProductoForm, Tipo_ProductoForm,
                    MaterialForm, LongitudForm, CalibreForm, FormaForm)

#Vistas de Producto y Detalle -----------------------------
def index(request):
    productos = Producto.objects.all()

    context = {
        "productos" : productos,
    }

    return render(request, 'producto/producto_list.html', context)

class ProductoDetail(DetailView):
    model = Producto
    template_name = 'producto/producto_detail.html'

class ProductoUpdate(UpdateView):
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

def producto(request):
    form = ProductoForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        form.save()
        return redirect('Producto:index')

    return render(request, 'producto/productos.html', context)

#--------------------------------------------------------

def lote(request):
    form = LoteForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        form.save()

    return render(request, 'producto/lote.html', context)

def tipo_producto(request):
    form = Tipo_ProductoForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        form.save()

    return render(request, 'producto/tipo_producto.html', context)

def material(request):
    form = MaterialForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        form.save()

    return render(request, 'producto/material.html', context)

def longitud(request):
    form = LongitudForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        form.save()

    return render(request, 'producto/longitud.html', context)

def calibre(request):
    form = CalibreForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        form.save()

    return render(request, 'producto/calibre.html', context)

def forma(request):
    form = FormaForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        form.save()

    return render(request, 'producto/forma.html', context)

def filtroProducto(request):
    id_marca = request.GET['id_marca']
    id_tipo = request.GET['id_tipo']


    productos = Producto.objects.filter(
                    Marca_id= id_marca,
                    Tipo_Producto_id= id_tipo
                    )

    data = serializers.serialize('json', productos)

    return HttpResponse(data, content_type='application/json')
