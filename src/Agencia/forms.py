from django import forms
from .models import Agencia, Vehiculo, Entrega, Mercaderia

class AgenciaForm(forms.ModelForm):
    class Meta:
        model = Agencia
        fields = ["nombre", "direccion", "capital", "Municipio_id"]

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ["marca", "modelo", "placa", "Agencia_id"]

class EntregaForm(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = ["kEntrada", "kSalida", "fecha", "vale", "Vehiculo_id"]

class MercaderiaForm(forms.ModelForm):
    class Meta:
        model = Mercaderia
        fields = ["Producto_id", "Agencia_id", "cantidad"]
