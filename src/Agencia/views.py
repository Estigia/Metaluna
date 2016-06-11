from django.shortcuts import render
from .models import Agencia, Vehiculo, Entrega, Mercaderia
from django.http import HttpResponse
from .forms import AgenciaForm, VehiculoForm, EntregaForm, MercaderiaForm

def Agencia(request):
    form = AgenciaForm(request.POST or None)

    context = {"form":form}

    return render(request, "agencia.html", context)


def Vehiculo(request):
    form = VehiculoForm()

    context = {"form": form}

    return render(request, "vehiculo.html", context)


def Entrega(request):
    form = EntregaForm()

    context = {"form": form}

    return render(request, "entrega.html", context)



def Mercaderia(request):
    form = MercaderiaForm()

    context = {"form": form}

    return render(request, "mercaderia.html", context)
