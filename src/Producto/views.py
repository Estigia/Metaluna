from django.shortcuts import render

from .forms import (LoteForm, ProductoForm, Tipo_ProductoForm,
                    MaterialForm, LongitudForm, CalibreForm, FormaForm)

def producto(request):
    form = ProductoForm(request.POST or None)
    Tipo_Producto = Tipo_Producto.objects.all()
    Material = Material.objects.all()
    Longitud = Longitud.objects.all()
    Calibre = Calibre.objects.all()
    Forma = Forma.objects.all()

    context = {
        "form" : form,
        "Tipo_Producto" : Tipo_Producto,
        "Material" : Material,
        "Longitud" : Longitud,
        "Calibre" : Calibre,
        "Forma" : Forma
    }

    if form.is_valid():
        form.save()

    return render(request, 'productos.html', context)

def lote(request):
    form = LoteForm(request.POST or None)
    Producto = Producto.objects.all()

    context = {
        "form" : form,
        "Producto" : Producto
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
