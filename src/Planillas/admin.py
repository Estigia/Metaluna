from django.contrib import admin

from .models import Planilla
from .forms import PlanillaForm
# Register your models here.
class PlanillaAdmin(admin.ModelAdmin):
    list_display = ["__unicode__"]
    form = PlanillaForm


admin.site.register(Planilla,PlanillaAdmin)
