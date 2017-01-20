from django.contrib import admin

from  .models import Puesto, Empleado, Usuario, Log_user
# Register your models here.

class PuestoAdmin(admin.ModelAdmin):
    list_display = ['id', 'puesto']

#class Tipo_UsuarioAdmin(admin.ModelAdmin):
#    list_display = ['id', 'tipo']

class Log_userAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'fecha']

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['id', '__unicode__', 'cui', 'nit', 'sueldo', 'Puesto_id', 'Agencia_id']

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', '__unicode__', 'username', 'Empleado_id', 'ultima_conexion']

admin.site.register(Puesto,PuestoAdmin)
#admin.site.register(Tipo_Usuario,Tipo_UsuarioAdmin)
admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Log_user, Log_userAdmin)
