from django.contrib import admin
from .models import Departamento, Municipio
# from .forms import MunicipioForm, DepartamentoForm
# Register your models here.

class AdminDepartamento(admin.ModelAdmin):
    list_display = ["id","departamento"]
    # form = DepartamentoForm

class AdminMunicipio(admin.ModelAdmin):
    list_display = ["id","municipio", "Departamento_id"]
    # form = MunicipioForm
    #* De esta manera se muestra el departamento al que pertenece el municipio

admin.site.register(Departamento, AdminDepartamento)
admin.site.register(Municipio, AdminMunicipio)
