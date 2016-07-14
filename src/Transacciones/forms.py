from django import forms
from django.utils import timezone

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
        "monto",
        "saldo",
        "fechaLimite",
        "fechaAprobacion",
        ]

        # def __init__(self, *args, **kwargs):
        #     super(CreditoForm, self).__init__(*args, **kwargs)
        #
        #     self.fields['fechaLimite'].widget = forms.Textarea(
        #         attrs = {
        #             'placeholder': str(timezone.now())
        #         }
        #     )
        #
        #     self.fields['fechaAprobacion'].widget = forms.Textarea(
        #         attrs = {
        #             'placeholder': str(timezone.now())
        #         }
        #     )
