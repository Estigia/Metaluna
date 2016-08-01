import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.contrib import messages

from  Transacciones.models import Factura,Recibo
from Comodin.models import Marca, Comodin
from Producto.models import Tipo_Producto, Producto , Lote
from Agencia.models import Mercaderia
from .models import Factura, DetalleFactura, Credito
from .forms import ReciboForm,AbonosForm,FacturaForm,DetalleFacturaForm,CreditoForm

@login_required(login_url='base')
def recibo(request):
    form = ReciboForm(request.POST or None)
    context = {
        "form":form,
    }

    if form.is_valid():
        form.save()

    return render(request, 'recibo.html', context)

@login_required(login_url='base')
def abonos(request):
    form = AbonosForm(request.POST or None)
    context={
        "form":form,
        "creditos": Credito.objects.filter(Factura_id__Comodin_id__tipo=0)
    }
    if form.is_valid():
        form.save(commit=False)
        credito = Credito.objects.get(id=request.POST['creditos'])

        monto = form.cleaned_data.get('monto')

        if monto > credito.saldo:
            messages.error(request,
                'El monto es mayor que el saldo del credito, Saldo:')
        else:
            credito.saldo -= monto
            credito.save()
            credito.Factura_id.Comodin_id.saldo = credito.Factura_id.Comodin_id.saldo - monto
            credito.Factura_id.Comodin_id.save()
            form.save()

    return render(request,'transacciones/abonos.html',context)

@login_required(login_url='base')
def factura(request):

    #usuario = request.user

    form = FacturaForm(request.POST or None)
    form2 = DetalleFacturaForm(request.POST or None)
    datos = Factura.objects.all()
    context = {
        "form" : form,
        "form2" : form2,
        "datos" : datos,
    }
    if form.is_valid():
        form.save()
    if form2.is_valid():
        form2.save()
    return render(request,'factura.html',context)

@login_required(login_url='base')
def detalleFactura(request):
    form = DetalleFacturaForm(request.POST or None)
    context = {
        "form":form,
    }
    if form.is_valid():
        form.save()
    return render(request,'detalleFactura.html',context)

@login_required(login_url='base')
def credito(request):

    if request.GET:
        factura = request.GET['factura']

        try:
            factura = Factura.objects.get(id=factura)

            try:
                credito = Credito.objects.get(Factura_id=factura)
                print 'try'
            except Credito.DoesNotExist:
                print str(timezone.now())

                form = CreditoForm(request.POST or None)

                context = {
                    "form":form,
                    }

                if form.is_valid():
                    print 'form'

                    form.save(commit=False)

                    credito = Credito.objects.create(
                        aprobado = True,
                        monto = form.cleaned_data["monto"],
                        saldo = form.cleaned_data["saldo"],
                        finalizado = False,
                        fechaLimite = form.cleaned_data["fechaLimite"],
                        fechaAprobacion = form.cleaned_data["fechaAprobacion"],
                        Usuario_id = request.user,
                        Factura_id = factura
                    )


                    factura.Comodin_id.saldo = factura.Comodin_id.saldo + credito.saldo
                    factura.Comodin_id.save()

                    credito.save()



                    return HttpResponse('Credito creado: ' + str(credito.id))

                return render(request,'transacciones/credito.html',context)

            return HttpResponse('Esa factura ya tiene un credito.')

        except Factura.DoesNotExist:
            return HttpResponse('No existe esa factura.')

    return HttpResponse('No sirve')

@login_required(login_url='base')
def trans(request):
    datos = Factura.objects.all()
    return render(request,'base.html',{"datos":datos})

@login_required(login_url='base')
def ventas(request):

    context = {
        'tipos': Tipo_Producto.objects.all(),
        'marcas': Marca.objects.all(),
        'clientes': Comodin.objects.filter(tipo=0)
    }

    return render(request, 'transacciones/ventas.html', context)

@login_required(login_url='base')
def compras(request):

    context = {
        'tipos': Tipo_Producto.objects.all(),
        'marcas': Marca.objects.all(),
        'proveedores': Comodin.objects.filter(tipo=1)
    }

    return render(request, 'transacciones/compras.html', context)

@login_required(login_url='base')
def venta(request):
    detalles = request.GET['detalles']
    cliente = request.GET['cliente']
    serie = request.GET['serie']
    numDoc = request.GET['num_doc']

    credito = str(request.GET['credito'])

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


    agencia.capital += factura.precioTotal
    agencia.save()


    f = Marca.objects.all()

    factura = Factura.objects.filter(id = factura.id)


    data = serializers.serialize('json', factura)

    return HttpResponse(data, content_type='application/json')

@login_required(login_url='base')
def compra(request):
    detalles = request.GET['detalles']
    proveedor = request.GET['proveedor']
    serie = request.GET['serie']
    numDoc = request.GET['num_doc']

    credito = str(request.GET['credito'])

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


    agencia.capital = agencia.capital - factura.precioTotal
    agencia.save()

    factura = Factura.objects.filter(id = factura.id)

    data = serializers.serialize('json', factura)




    return HttpResponse(data, content_type='application/json')



@login_required(login_url='base')
def index(request):

    context = {
    }

    return render(request, 'transacciones/transacciones.html', context)


def facturaList(request, tipo):

    if tipo == 'compras':
        facturas = Factura.objects.filter(Comodin_id__tipo=1)
        mensaje = 'compras'
    if tipo == 'ventas':
        facturas = Factura.objects.filter(Comodin_id__tipo=0)
        mensaje = 'ventas'

    return render(
            request,
            'transacciones/facturas_list.html',
            {
                'facturas':facturas,
                'mensaje': mensaje
                }
            )

class FacturaDetail(DetailView):
    model = Factura
    template_name = 'transacciones/factura_detail.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(FacturaDetail, self).dispatch(request, *args, **kwargs)
