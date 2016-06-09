from django.contrib import admin

from .models import Comodin, Marca
# Register your models here.

class ComodinAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        '__unicode__',
        'direccion',
        'telefono',
        'nit',
        'tipo',
        'bloqueado',
        'saldo',
        ]

class MarcaAdmin(admin.ModelAdmin):
    list_display = ['id', 'marca', 'Comodin_id']

admin.site.register(Comodin, Comodin_id)
admin.site.register(Marca, MarcaAdmin)
