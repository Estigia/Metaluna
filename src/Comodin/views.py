from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.core import serializers
from django.http import HttpResponse

from .models import Comodin, Marca

class ComodinCreate(CreateView):
    model = Comodin
    template_name = 'comodin_create.html'
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

    def form_valid(self, form):
        p = form.save(commit = False)

        p.tipo = False

        self.object = p.save()

        return super(ComodinCreate, self).form_valid(form)


class ClienteCreate(ComodinCreate):

    def form_valid(self, form):
        p = form.save(commit = False)

        p.tipo = True

        self.object = p.save()

        return super(ClienteCreate, self).form_valid(form)

class MarcaCreate(CreateView):
    model = Marca
    template_name = 'marca_create.html'
    success_url = '/marca'

    fields = ['marca']

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

def filtroP(request):
    proveedores = Comodin.objects.filter(tipo=False)
    print proveedores
    data = serializers.serialize('json', proveedores, fields = ('marca'))

    return HttpResponse(data, content_type = 'application/json')
