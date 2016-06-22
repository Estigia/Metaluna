from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView

from .models import Agencia, Vehiculo, Entrega, Mercaderia
from .forms import AgenciaForm, VehiculoForm, EntregaForm, MercaderiaForm

#Vistas de Agencia y detalles---------------------------------
def agencia(request):
    form = AgenciaForm(request.POST or None)

    context = {"form":form}

    return render(request, "agencia.html", context)

class AgenciaDetail(DetailView):
    model = Agencia
    template_name = 'agencia_detail.html'

def index(request):
    agencias = Agencia.objects.all()

    context = {
        'agencias': agencias,
    }

    return render(request, 'agencia_list.html', context)

class AgenciaUpdate(UpdateView):
    model = Agencia
    template_name = 'agencia_edit.html'
    success_url = reverse_lazy('Agencia:index')

    fields = [

        'nombre',
        'direccion',
        'capital',
        'Municipio_id',

    ]

#-------------------------------------------------------------
#Vistas de Vehiculos------------------------------------------

def vehiculo(request):
    form = VehiculoForm()

    context = {"form": form}

    return render(request, "vehiculo.html", context)


def entrega(request):
    form = EntregaForm()

    context = {"form": form}

    return render(request, "entrega.html", context)



def mercaderia(request):
    form = MercaderiaForm()

    context = {"form": form}

    return render(request, "mercaderia.html", context)
