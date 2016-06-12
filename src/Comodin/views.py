from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.core import serializers
from django.http import HttpResponse

from .models import Comodin, Marca

class ComodinCreate(CreateView):
    model = Comodin
    template_name = 'comodin_create.html'

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

    fields = ['marca', 'Comodin_id']

def filtroP(request):
    proveedores = Comodin.objects.filter(Comodin_id=False)

    data = serializers.serialize('json', proveedores, fields = ('marca'))

    return HttpResponse(data, content_type = 'application/json')
