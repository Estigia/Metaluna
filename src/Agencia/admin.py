from django.contrib import admin
from .models import Agencia, Vehiculo, Entrega, Mercaderia
# Register your models here.

class AgenciaAdmin(admin.ModelAdmin):
    list_display = ["id","nombre", "direccion", "capital", "Municipio_id"]

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ["id", "marca", "modelo", "placa", "Agencia_id"]

class EntregaAdmin(admin.ModelAdmin):
    list_display = ["id", "kEntrada", "kSalida", "fecha", "vale", "Vehiculo_id"]

class MercaderiaAdmin(admin.ModelAdmin):
    list_display = ["id", "Producto_id", "Agencia_id", "cantidad"]

admin.site.register(Agencia, AgenciaAdmin)
admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Entrega, EntregaAdmin)
admin.site.register(Mercaderia, MercaderiaAdmin)
