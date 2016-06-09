from django.contrib import admin
from .forms import ReciboForm,FacturaForm,DetalleFacturaForm,CreditoForm,AbonosForm
# Register your models here.
from .models import Recibo,Factura,DetalleFactura,Credito,Abonos

class ReciboAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","noDocumento"]
    form = ReciboForm

class AbonosAdmin(admin.ModelAdmin):
    list_display = ["__unicode__"]
    form = AbonosForm

class FacturaAdmin(admin.ModelAdmin):
    list_display = ["__unicode__"]
    form = FacturaForm

class DetalleFacturaAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","cantidad","subTotal"]
    form = DetalleFacturaForm

class CreditoAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","aprobado"]
    form = CreditoForm

admin.site.register(Recibo,ReciboAdmin)
admin.site.register(Abonos,AbonosAdmin)
admin.site.register(Factura,FacturaAdmin)
admin.site.register(DetalleFactura,DetalleFacturaAdmin)
admin.site.register(Credito,CreditoAdmin)
