from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.views.generic.edit import UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, ListView

from .models import Agencia, Vehiculo, Entrega, Mercaderia
from .forms import AgenciaForm, VehiculoForm, EntregaForm, MercaderiaForm
from Usuario.models import Empleado

#Vistas de Agencia y detalles---------------------------------
@login_required(login_url='base')
def agencia(request):
    if not request.user.is_staff:
        return HttpResponseRedirect('/')

    form = AgenciaForm(request.POST or None)

    context = {"form":form}

    if form.is_valid():
        form.save()
        return redirect("Agencia:index")

    return render(request, "agencia/agencia.html", context)

class AgenciaDetail(DetailView):
    model = Agencia
    template_name = 'agencia/agencia_detail.html'

    # def get_queryset(self):
    #     self.agencia = get_object_or_404(Agencia, id=self.args[0])
    #     return Empleado.objects.filter(agencia=self.agencia)

    def get_context_data(self, **kwargs):
        context = super(AgenciaDetail, self).get_context_data(**kwargs)
        context.update({'empleados' : Empleado.objects.all()}) #['empleados'] = Empleado.objects.all()
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseRedirect('/')

        return super(AgenciaDetail, self).dispatch(request, *args, **kwargs)

@login_required(login_url='base')
def index(request):
    if not request.user.is_staff:
        return HttpResponseRedirect('/')

    agencias = Agencia.objects.all()

    context = {
        'agencias': agencias,
    }

    return render(request, 'agencia/agencia_list.html', context)

class AgenciaEmpleadoList(ListView):
    model = Agencia
    context_object_name = "empleados_list"
    template_name = "agencia/empleados_por_agencia.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseRedirect('/')

        return super(AgenciaEmpleadoList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        valor = 0
        for key, value in self.kwargs.iteritems():
            valor = value

        agencia = get_object_or_404(Agencia, nombre__iexact = Agencia.objects.get(id=valor))
        return Empleado.objects.filter(Agencia_id=agencia)
    #
    # def get_context_data(self, **kwargs):
    #     print kwargs
    #     print kwargs
    #     print kwargs
    #     print kwargs
    #     context = super(AgenciaEmpleadoList, self).get_context_data(**kwargs)
    #     #context.update({'agencia' : Agencia.objects.get(id=valor)})
    #     return context
    #

class AgenciaProductoList(ListView):
    model = Agencia
    context_object_name = "productos_list"
    template_name = "agencia/productos_por_agencia.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseRedirect('/')

        return super(AgenciaProductoList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        valor = 0
        for key, value in self.kwargs.iteritems():
            valor = value

        self.agencia = get_object_or_404(Agencia, nombre__iexact = Agencia.objects.get(id=valor))
        return Mercaderia.objects.filter(Agencia_id=self.agencia)

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

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseRedirect('/')

        return super(AgenciaUpdate, self).dispatch(request, *args, **kwargs)

#-------------------------------------------------------------
#Vistas de Vehiculos------------------------------------------
@login_required(login_url='base')
def vehiculo(request):
    form = VehiculoForm(request.POST or None)

    context = {"form": form}

    if form.is_valid():
        form.save()

        return redirect("Agencia:list_v")

    return render(request, "agencia/vehiculo.html", context)

class VehiculoDetail(DetailView):
    model = Vehiculo
    template_name = 'agencia/vehiculo_detail.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(VehiculoDetail, self).dispatch(request, *args, **kwargs)

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

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(VehiculoUpdate, self).dispatch(request, *args, **kwargs)

@login_required(login_url='base')
def vehiculoList(request):
    vehiculos = Vehiculo.objects.all()

    context = {
        'vehiculos': vehiculos,
    }

    return render(request,'agencia/vehiculo_list.html', context)

#-------------------------------------------------------------
#Vistas de Entrega--------------------------------------------
@login_required(login_url='base')
def entrega(request):
    form = EntregaForm(request.POST or None, initial={'fecha': timezone.now()})

    context = {"form": form}

    if form.is_valid():
        form.save()
        return redirect("Agencia:list_v")
        #aca agregue el form save
    else:
        print "popo"

    return render(request, "agencia/entrega.html", context)

@login_required(login_url='base')
def entregaList(request, vehiculo_id):
    entregas = Entrega.objects.filter(Vehiculo_id = vehiculo_id)

    context = {
        'entregas': entregas,
    }

    return render(request, 'agencia/entrega_list.html', context)

class EntregaDetail(DetailView):
    model = Entrega
    template_name = 'agencia/entrega_detail.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(EntregaDetail, self).dispatch(request, *args, **kwargs)

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

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(EntregaUpdate, self).dispatch(request, *args, **kwargs)
#-------------------------------------------------------------
#Vistas de Mercaderia-----------------------------------------
@login_required(login_url='base')
def mercaderia(request):
    form = MercaderiaForm()

    context = {"form": form}

    return render(request, "agencia/mercaderia.html", context)

@login_required(login_url='base')
def mercaderiaList(request):
    mercaderia = Mercaderia.objects.all()

    context = {
        'mercaderia': mercaderia,
    }

    return render(request, 'agencia/mercaderia_list.html', context)

class MercaderiaDetail(DetailView):
    model = Mercaderia
    template_name = 'agencia/mercaderia_detail.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(MercaderiaDetail, self).dispatch(request, *args, **kwargs)

class MercaderiaUpdate(UpdateView):
    model = Mercaderia
    template_name = 'agencia/mercaderia_edit.html'
    success_url = reverse_lazy('Agencia:list_m')

    fields = [
        'Producto_id',
        'Agencia_id',
        'cantidad',
    ]
def impresion(request):
    vehiculos = Vehiculo.objects.all()

    context = {
        'vehiculos': vehiculos,
    }
    return render(request, "agencia/impresionEntrega.html",context)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(MercaderiaUpdate, self).dispatch(request, *args, **kwargs)
#-----------------------------------------------------------
