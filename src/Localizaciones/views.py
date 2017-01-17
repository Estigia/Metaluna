from django.shortcuts import render
from django.core import serializers
from .models import Municipio, Departamento
from django.http import HttpResponse
# # Create your views here.
#
# def Localizacion(request):
#     Departamentos = Departamento.objects.all()
#     Municipios = Municipio.objects.all()
#
#     context = {
#         "Departamentos": Departamentos,
#         "Municipios": Municipios,
#         "titulo": "Localizacion"
#     }
#
#     return render(request, 'localizacion.html', context)
#
def BusquedaMunicipio(request):
    id_Departamento = request.GET['id']
    muni = Municipio.objects.filter(Departamento_id= id_Departamento)
    #print muni
    data = serializers.serialize('json', muni, fields =('municipio'))
    #print data
    return HttpResponse(data, content_type='application/json')
