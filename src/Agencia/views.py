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

    return render(request, "agencia/agencia.html", context)

class AgenciaDetail(DetailView):
    model = Agencia
    template_name = 'agencia/agencia_detail.html'

def index(request):
    agencias = Agencia.objects.all()

    context = {
        'agencias': agencias,
    }

    return render(request, 'agencia/agencia_list.html', context)

class AgenciaUpdate(UpdateView):
    model = Agencia
    template_name = 'agencia/agencia_edit.html'
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

    return render(request, "agencia/vehiculo.html", context)

class VehiculoDetail(DetailView):
    model = Vehiculo
    template_name = 'agencia/vehiculo_detail.html'

class VehiculoUpdate(UpdateView):
    model = Vehiculo
    template_name = 'agencia/vehiculo_edit.html'
    success_url = reverse_lazy('Agencia:list_v')

    fields = [

        'marca',
        'modelo',
        'placa',
        'Agencia_id',

    ]

def vehiculoList(request):
    vehiculos = Vehiculo.objects.all()

    context = {
        'vehiculos': vehiculos,
    }

    return render(request,'agencia/vehiculo_list.html', context)

#-------------------------------------------------------------
#Vistas de Entrega--------------------------------------------

def entrega(request):
    form = EntregaForm()

    context = {"form": form}

    return render(request, "agencia/entrega.html", context)

def entregaList(request):
    entregas = Entrega.objects.all()

    context = {
        'entregas': entregas,
    }

    return render(request, 'agencia/entrega_list.html', context)

class EntregaDetail(DetailView):
    model = Entrega
    template_name = 'agencia/entrega_detail.html'

class EntregaUpdate(UpdateView):
    model = Entrega
    template_name = 'agencia/entrega_edit.html'
    success_url = reverse_lazy('Agencia:list_e')

    fields = [
        'kEntrada',
        'kSalida',
        'fecha',
        'vale',
        'Vehiculo_id',
    ]
#-------------------------------------------------------------
#Vistas de Mercaderia-----------------------------------------

def mercaderia(request):
    form = MercaderiaForm()

    context = {"form": form}

    return render(request, "agencia/mercaderia.html", context)

def mercaderiaList(request):
    mercaderia = Mercaderia.objects.all()

    context = {
        'mercaderia': mercaderia,
    }

    return render(request, 'agencia/mercaderia_list.html', context)

class MercaderiaDetail(DetailView):
    model = Mercaderia
    template_name = 'agencia/mercaderia_detail.html'

class MercaderiaUpdate(UpdateView):
    model = Mercaderia
    template_name = 'agencia/mercaderia_edit.html'
    success_url = reverse_lazy('Agencia:list_m')

    fields = [
        'Producto_id',
        'Agencia_id',
        'cantidad',
    ]
#-----------------------------------------------------------
