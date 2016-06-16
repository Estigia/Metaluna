from django import forms
from .models import Planilla

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
