from django.shortcuts import render


from .forms import ReciboForm,AbonosForm,FacturaForm,DetalleFacturaForm,CreditoForm
from  Transacciones.models import Factura,Recibo
# Create your views here.
def recibo(request):
    form = ReciboForm(request.POST or None)
    context = {
        "form":form,
    }

    if form.is_valid():
        form.save()

    return render(request, 'recibo.html', context)

def abonos(request):
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

def detalleFactura(request):
    form = DetalleFacturaForm(request.POST or None)
    context = {
        "form":form,
    }
    if form.is_valid():
        form.save()
    return render(request,'detalleFactura.html',context)

def credito(request):
    form = CreditoForm(request.POST or None)
    context = {

    "form":form,

    }

    if form.is_valid():
        form.save()
    return render(request,'credito.html',context)

def trans(request):
    datos = Factura.objects.all()
    return render(request,'base.html',{"datos":datos})
