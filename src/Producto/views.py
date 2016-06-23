from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse, reverse_lazy

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

    return render(request, 'producto_list.html', context)

class ProductoDetail(DetailView):
    model = Producto
    template_name = 'producto_detail.html'

def producto(request):
    form = ProductoForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        form.save()

    return render(request, 'productos.html', context)

#--------------------------------------------------------

def lote(request):
    form = LoteForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        form.save()

    return render(request, 'lote.html', context)

def tipo_producto(request):
    form = Tipo_ProductoForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        form.save()

    return render(request, 'tipo_producto.html', context)

def material(request):
    form = MaterialForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        form.save()

    return render(request, 'material.html', context)

def longitud(request):
    form = LongitudForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        form.save()

    return render(request, 'longitud.html', context)

def calibre(request):
    form = CalibreForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        form.save()

    return render(request, 'calibre.html', context)

def forma(request):
    form = FormaForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        form.save()

    return render(request, 'forma.html', context)
