from django import forms
from .models import Planilla, Finanzas

class PlanillaForm(forms.ModelForm):
    class Meta:
        model = Planilla
        fields = [
        "sueldo",
        "horasExtra",
        "bonoIncentivo",
        "igss",
        "isr",
        "anticipos",
        "judiciales",
        "otros",
        "totalDescuento",
        "totalLiquido",
        "Empleado_id",
        "Agencia_id",
        ]

class FinanzasForm(forms.ModelForm):
    class Meta:
        model = Finanzas
        fields = {
            "descripcion",
            "tipo",
            "monto",
        }
