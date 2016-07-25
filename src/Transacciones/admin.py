from django.contrib import admin
from .forms import ReciboForm,FacturaForm,DetalleFacturaForm,CreditoForm,AbonosForm
# Register your models here.
from .models import Recibo,Factura,DetalleFactura,Credito,Abonos

class ReciboAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","noDocumento"]
    form = ReciboForm

class AbonosAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","monto","fecha","Credito_id"]
    form = AbonosForm

class FacturaAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","serie","noDocumento","precioTotal","anulada","Comodin_id"]
    form = FacturaForm

class DetalleFacturaAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","cantidad","subTotal","Factura_id","Producto_id"]
    form = DetalleFacturaForm

class CreditoAdmin(admin.ModelAdmin):
    list_display = [
        "__unicode__",
        "aprobado",
        "monto",
        "saldo",
        "finalizado",
        "fechaLimite",
        "fechaAprobacion",
        ]
        #"Usuario_id",]
        #"Factura_id",]
        #]
    form = CreditoForm

admin.site.register(Recibo,ReciboAdmin)
admin.site.register(Abonos,AbonosAdmin)
admin.site.register(Factura,FacturaAdmin)
admin.site.register(DetalleFactura,DetalleFacturaAdmin)
admin.site.register(Credito,CreditoAdmin)
