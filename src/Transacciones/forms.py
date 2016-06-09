from django import forms
from .models import Factura,DetalleFactura,Recibo,Abonos,Credito

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = [
        "serie",
        "noDocumento",
        "precioTotal",
        ]

class DetalleFacturaForm(forms.ModelForm):
    class Meta:
        model = DetalleFactura
        fields = [
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
        ]

class CreditoForm(forms.ModelForm):
    class Meta:
        model = Credito
        fields = [
        "monto",
        "saldo",
        "fechaLimite",
        ]
