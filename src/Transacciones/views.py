import json

from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from Comodin.models import Marca, Comodin
from Producto.models import Tipo_Producto, Producto
from Agencia.models import Mercaderia
from .models import Factura, DetalleFactura
from .forms import ReciboForm,AbonosForm,FacturaForm,DetalleFacturaForm,CreditoForm

def Recibo(request):
    form = ReciboForm(request.POST or None)
    context = {
        "form":form,
    }

    if form.is_valid():
        form.save()

    return render(request, 'recibo.html', context)

def Abonos(request):
    form = AbonosForm(request.POST or None)
    context={
        "form":form,
    }
    if form.is_valid():
        form.save()
    return render(request,'abonos.html',context)

def factura(request):
    form = FacturaForm(request.POST or None)
    form2 = DetalleFacturaForm(request.POST or None)
    context = {
        "form" : form,
        "form2" : form2,
    }
    if form.is_valid():
        form.save()
    if form2.is_valid():
        form2.save()
    return render(request,'factura.html',context)

def detalleFactura(request):
    form = DetalleFacturaForm(request.POST or None)
    context = {
        "form":form,
    }
    if form.is_valid():
        form.save()
    return render(request,'detalleFactura.html',context)

def Credito(request):
    form = CreditoForm(request.POST or None)
    context = {

    "form":form,

    }

    if form.is_valid():
        form.save()
    return render(request,'credito.html',context)

def trans(request):
    return render(request,'base.html',{})

def ventas(request):

    context = {
        'tipos': Tipo_Producto.objects.all(),
        'marcas': Marca.objects.all(),
        'clientes': Comodin.objects.filter(tipo=0)
    }

    return render(request, 'transacciones/ventas.html', context)

def compras(request):

    context = {
        'tipos': Tipo_Producto.objects.all(),
        'marcas': Marca.objects.all(),
        'proveedores': Comodin.objects.filter(tipo=1)
    }

    return render(request, 'transacciones/compras.html', context)

def venta(request):
    detalles = request.GET['detalles']
    cliente = request.GET['cliente']
    serie = request.GET['serie']
    numDoc = request.GET['num_doc']

    comodin = Comodin.objects.get(id=cliente)
    factura = Factura.objects.create(
                serie=serie,
                noDocumento=numDoc,
                anulada=False,
                Comodin_id=comodin
                )

    factura.save()

    data = json.loads(detalles)

    agencia = request.user.Empleado_id.Agencia_id

    total = 0
    for majorkey, subdict in data.iteritems():
        detalle = DetalleFactura()
        for subkey, value in subdict.iteritems():
            if subkey == 'cantidad':
                detalle.cantidad = value
            elif subkey == 'descripcion':
                producto = Producto.objects.get(id=value)
                detalle.Producto_id = producto
            elif subkey == 'subtotal':
                total += value
                detalle.subTotal = value

        mercaderia = Mercaderia.objects.get(
                                        Agencia_id=agencia,
                                        Producto_id=detalle.Producto_id
                                        )

        mercaderia.cantidad -= detalle.cantidad

        mercaderia.save()
        detalle.Factura_id = factura
        detalle.save()

    factura.precioTotal = total
    factura.save()

    f = Marca.objects.all()

    data = serializers.serialize('json', f)

    return HttpResponse(data, content_type='application/json')

def compra(request):
    detalles = request.GET['detalles']
    proveedor = request.GET['proveedor']
    serie = request.GET['serie']
    numDoc = request.GET['num_doc']

    comodin = Comodin.objects.get(id=proveedor)
    factura = Factura.objects.create(
                serie=serie,
                noDocumento=numDoc,
                anulada=False,
                Comodin_id=comodin
                )

    factura.save()

    data = json.loads(detalles)

    agencia = request.user.Empleado_id.Agencia_id

    total = 0
    for majorkey, subdict in data.iteritems():
        detalle = DetalleFactura()
        for subkey, value in subdict.iteritems():
            if subkey == 'cantidad':
                detalle.cantidad = value
            elif subkey == 'descripcion':
                producto = Producto.objects.get(id=value)
                detalle.Producto_id = producto
            elif subkey == 'subtotal':
                total += value
                detalle.subTotal = value

        mercaderia = Mercaderia.objects.get(
                                        Agencia_id=agencia,
                                        Producto_id=detalle.Producto_id
                                        )

        print mercaderia.cantidad
        mercaderia.cantidad += detalle.cantidad
        print mercaderia.cantidad
        mercaderia.save()
        detalle.Factura_id = factura
        detalle.save()

    factura.precioTotal = total
    factura.save()

    f = Marca.objects.all()

    data = serializers.serialize('json', f)

    return HttpResponse(data, content_type='application/json')
