#encoding: utf-8

import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.contrib import messages

from  Transacciones.models import Factura,Recibo
from Comodin.models import Marca, Comodin
from Producto.models import Tipo_Producto, Producto , Lote
from Agencia.models import Mercaderia
from .models import Factura, DetalleFactura, Credito, Abonos
from .forms import ReciboForm,AbonosForm,FacturaForm,DetalleFacturaForm,CreditoForm

@login_required(login_url='base')
def recibo(request):
    if not request.user.is_staff:
        return HttpResponseRedirect('/')

    form = ReciboForm(request.POST or None)
    context = {
        "form":form,
    }

    if form.is_valid():
        form.save()

    return render(request, 'recibo.html', context)

@login_required(login_url='base')
def abonos(request, tipo):
    if not request.user.is_staff:
        return HttpResponseRedirect('/')

    if tipo == 'compras':
        creditos=Credito.objects.filter(Factura_id__Comodin_id__tipo=1)
    else:
        creditos=Credito.objects.filter(Factura_id__Comodin_id__tipo=0)

    creditos = creditos.filter(finalizado=0)
    form = AbonosForm(request.POST or None)
    context={
        "form":form,
        "creditos": creditos
    }
    if form.is_valid():
        form.save(commit=False)
        credito = Credito.objects.get(id=request.POST['creditos'])

        monto = form.cleaned_data.get('monto')

        if monto > credito.saldo:
            messages.error(request,
                'El monto es mayor que el saldo del credito, Saldo:'+str(credito.saldo))
        else:
            credito.saldo -= monto

            if credito.saldo == 0:
                print 'monto 0'
                credito.finalizado = 1
            credito.save()
            credito.Factura_id.Comodin_id.saldo = credito.Factura_id.Comodin_id.saldo - monto
            credito.Factura_id.Comodin_id.save()
            abono = Abonos.objects.create(
                monto=monto,
                Credito_id=credito
            )

            if tipo=='compras':
                return HttpResponseRedirect('/transacciones/compras/abonos')
            else:
                return HttpResponseRedirect('/transacciones/ventas/abonos')

    return render(request, 'transacciones/abonos.html', context)

@login_required(login_url='base')
def abonosList(request, tipo):
    if not request.user.is_staff:
        return HttpResponseRedirect('/')

    if tipo == 'compras':
        abonos = Abonos.objects.filter(
            Credito_id__Factura_id__Comodin_id__tipo = 1
        )
    else:
        abonos = Abonos.objects.filter(
            Credito_id__Factura_id__Comodin_id__tipo = 0
        )

    context = {
        'abonos': abonos,
    }

    return render(request, 'transacciones/abonos_list.html', context)

class AbonoDetail(DetailView):
    model = Abonos
    template_name = 'transacciones/abono_detail.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseRedirect('/')
        return super(AbonoDetail, self).dispatch(request, *args, **kwargs)

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
    print timezone.now()
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



                    messages.info(request,
                        'Credito creado: ' + str(credito.id))
                    return HttpResponseRedirect('/transacciones/')

                return render(request,'transacciones/credito.html',context)

            messages.error(request,
                'Esa factura ya tiene un credito.')
            return HttpResponseRedirect('/transacciones/')

        except Factura.DoesNotExist:
            messages.error(request,
                'No existe esa factura.')
            return HttpResponseRedirect('/transacciones/')

    messages.error(request,
        'Ocurrió un error.')
    return HttpResponseRedirect('/transacciones/')

@login_required(login_url='base')
def trans(request):
    if not request.user.is_staff:
        return HttpResponseRedirect('/')
    datos = Factura.objects.all()
    return render(request,'base.html',{"datos":datos})

@login_required(login_url='base')
def ventas(request):

    context = {
        'tipos': Tipo_Producto.objects.all(),
        'marcas': Marca.objects.all(),
        'clientes': Comodin.objects.filter(tipo=0),
        'noDoc': Factura.objects.filter(Comodin_id__tipo=0).count() + 1
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
    numDoc = request.GET['num_doc']

    comodin = Comodin.objects.get(id=cliente)
    factura = Factura.objects.create(
                serie='A',
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


    factura = Factura.objects.filter(id = factura.id)


    data = serializers.serialize('json', factura)

    return HttpResponse(data, content_type='application/json')

@login_required(login_url='base')
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

        try:
            mercaderia = Mercaderia.objects.get(
                            Agencia_id=agencia,
                            Producto_id=detalle.Producto_id
                            )
        except:
            mercaderia = Mercaderia.objects.create(
                Agencia_id = agencia,
                Producto_id = detalle.Producto_id,
                cantidad = 0
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

@login_required(login_url='base')
def facturaList(request, tipo):
    if not request.user.is_staff:
        return HttpResponseRedirect('/')

    if tipo == 'compras':
        comodines = Comodin.objects.filter(tipo=1)
        facturas = Factura.objects.filter(Comodin_id__tipo=1)
        mensaje = 'compras'
    if tipo == 'ventas':
        comodines = Comodin.objects.filter(tipo=0)
        facturas = Factura.objects.filter(Comodin_id__tipo=0)
        mensaje = 'ventas'

    if request.GET:
        try:
            facturas = facturas.filter(serie__iexact=request.GET['serie'])
        except:
            pass
        try:
            facturas = facturas.filter(noDocumento=request.GET['numero'])
        except:
            pass
        try:
            facturas = facturas.filter(Comodin_id__id=request.GET['comodin'])
        except:
            pass
        try:
            facturas = facturas.filter(anulada=request.GET['anulada'])
        except:
            pass


    return render(
            request,
            'transacciones/facturas_list.html',
            {
                'facturas':facturas,
                'mensaje': mensaje,
                'comodines': comodines
            }
        )

class FacturaDetail(DetailView):
    model = Factura
    template_name = 'transacciones/factura_detail.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseRedirect('/')
        return super(FacturaDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super(FacturaDetail, self).get_context_data(**kwargs)

        factura = self.get_object(self.queryset)

        detalles = DetalleFactura.objects.filter(Factura_id=factura)

        total = detalles.aggregate(Sum('subTotal'))

        context.update({
            'detalles': detalles,
            'total': total
        })

        return context

def creditoList(request, tipo):
    if not request.user.is_staff:
        return HttpResponseRedirect('/')
    if tipo == 'compras':
        creditos = Credito.objects.filter(Factura_id__Comodin_id__tipo=1)
        mensaje = 'compras'
    if tipo == 'ventas':
        creditos = Credito.objects.filter(Factura_id__Comodin_id__tipo=0)
        mensaje = 'ventas'

    return render(
            request,
            'transacciones/credito_list.html',
            {
                'creditos':creditos,
                'mensaje': mensaje
                }
            )

class CreditoProveedorDetail(DetailView):
    model = Credito
    template_name = 'transacciones/credito_detail.html'
    queryset = Credito.objects.filter(Factura_id__Comodin_id__tipo=1)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseRedirect('/')
        return super(CreditoProveedorDetail, self).dispatch(request, *args, **kwargs)

class CreditoClienteDetail(DetailView):
    model = Credito
    template_name = 'transacciones/credito_detail.html'
    queryset = Credito.objects.filter(Factura_id__Comodin_id__tipo=0)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseRedirect('/')
        return super(CreditoClienteDetail, self).dispatch(request, *args, **kwargs)

@login_required(login_url='base')
def anular(request):
    vID = request.GET['id']
    factura = Factura.objects.get(id=vID)

    factura.anulada = not factura.anulada
    factura.save()

    if factura.anulada:
        response = 'Factura anulada: '+vID
    else:
        response = 'Factura recuperada: '+vID

    # messages.info(request, 'Factura anulada:'+vID)
    #
    # data = serializers.serialize('json', messages)

    return HttpResponse(response)
