from django.shortcuts import render

# Create your views here.
def Recibo(request):
    form = ReciboForm(request.POST or None)
    context = {
    }

    if form.is_valid():
        form.save()

    return render(request, 'recibo.html', context)

def Abonos(request):
    form = AbonosForm(request.POST or None)
    context={

    }
    if form.is_valid():
        form.save()
        return render(request,'abonos.html',context)

def Factura(request):
    form = FacturaForm(request.POST or None)
    context = {

    }
    if form.is_valid():
        form.save()
        return render(request,'factura.html',context)

def DetalleFacturaForm(request):
    form = DetalleFacturaForm(request.POST or None)
    context = {

    }
    if form.is_valid():
        form.save()
        return render(request,'detalleFactura.html',context)

def Credito(request):
    form = CreditoForm(request.POST or None)
    context = {

    }
    if from.is_valid():
        form.save()
        return render(request,'credito.html',context)
