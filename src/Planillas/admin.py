from django.contrib import admin

from .models import Planilla, Finanzas
from .forms import PlanillaForm, FinanzasForm
# Register your models here.
class PlanillaAdmin(admin.ModelAdmin):
    list_display = ["__unicode__"]
    form = PlanillaForm

class FinanzasAdmin(admin.ModelAdmin):
    list_display = ["id","tipo","monto","descripcion"]
    form = FinanzasForm

admin.site.register(Planilla,PlanillaAdmin)
admin.site.register(Finanzas,FinanzasAdmin)
