from django import forms
from .models import Factura,DetalleFactura,Recibo,Abonos,Credito

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = [
        "serie",
        "noDocumento",
        "precioTotal",
        "anulada",
        "Comodin_id",
        ]

class DetalleFacturaForm(forms.ModelForm):
    class Meta:
        model = DetalleFactura
        fields = [
        "Factura_id",
        "Producto_id",
        "subTotal",
        "cantidad",
        ]

class ReciboForm(forms.ModelForm):
    class Meta:
        model = Recibo
        fields = [
        "noDocumento",
        ]

class AbonosForm(forms.ModelForm):
    class Meta:
        model = Abonos
        fields = [
        "monto",
        "fecha",
        "Credito_id",
        ]

class CreditoForm(forms.ModelForm):
    class Meta:
        model = Credito
        fields = [
        "aprobado",
        "monto",
        "saldo",
        "finalizado",
        "fechaLimite",
        "fechaAprobacion",
        "Usuario_id",
        "Factura_id",
        ]
