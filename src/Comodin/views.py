from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.core import serializers
from django.http import HttpResponse
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView, ListView

from .models import Comodin, Marca






@login_required(login_url='base')
def index(request):
    comodin = Comodin.objects.all().filter(tipo = True)

    context = {
        'comodin': comodin,
    }

    return render(request, 'comodin/proveedor_list.html', context)

def clientes(request):
    comodin = Comodin.objects.all().filter(tipo = False)

    context = {
        'comodin': comodin,
    }

    return render(request, 'comodin/clientes_list.html', context)

class ComodinCreate(CreateView):
    model = Comodin
    template_name = 'comodin/comodin_create.html'
    success_url = '/proveedor'

    fields = [
        'nombre',
        'empresa',
        'empresa',
        'direccion',
        'telefono',
        'nit',
        'saldo',
        ]

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ComodinCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        p = form.save(commit = False)

        p.tipo = True

        self.object = p.save()

        return super(ComodinCreate, self).form_valid(form)


class ClienteCreate(CreateView):
    model = Comodin
    template_name = 'comodin/comodin_create.html'
    success_url = '/cliente'

    fields = [
        'nombre',
        'empresa',
        'empresa',
        'direccion',
        'telefono',
        'nit',
        'saldo',
        ]

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ClienteCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        p = form.save(commit = False)

        p.tipo = False

        self.object = p.save()

        return super(ClienteCreate, self).form_valid(form)

class MarcaCreate(CreateView):
    model = Marca
    template_name = 'comodin/marca_create.html'
    success_url = '/marca'

    fields = ['marca']

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(MarcaCreate, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

       context = super(MarcaCreate, self).get_context_data(**kwargs)
       proveedores = Comodin.objects.filter(tipo = False)

       context.update({
            "proveedores": proveedores,
       })

       return context

    def form_valid(self, form):

        m = form.save(commit = False)
        vID = self.request.POST['proveedor_id']

        vID = Comodin.objects.get(id=vID)

        print vID

        m.Comodin_id = vID

        self.object = m.save()

        return super(MarcaCreate, self).form_valid(form)

class ComodinProveedorList(ListView):
    model = Comodin
    context_object_name = "comodin_list"
    template_name = "comodin/proveedor_list.html"

    def get_queryset(self):
        valor = 0
        for key, value in self.kwargs.iteritems():
            valor = value

        self.comodin = get_object_or_404(Comodin, nombre__iexact = Comodin.objects.get(id=valor))
        return Comodin.objects.filter(tipo=True)

@login_required(login_url='base')
def filtroP(request):
    proveedores = Comodin.objects.filter(tipo=False)
    print proveedores
    data = serializers.serialize('json', proveedores, fields = ('marca'))

    return HttpResponse(data, content_type = 'application/json')
