from django import forms
from .models import Lote, Producto, Tipo_Producto,
                    Material, Longitud, Calibre, Forma

class LoteForm(forms.ModelForm):
    class Meta:
        model = Lote
        fields = [
            "precio_compra",
            "Producto_id",
        ]

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            "descripcion",
            "Tipo_Producto_id",
            "Material_id",
            "Longitud_id",
            "Calibre_id",
            "Forma_id",
            "Marca_id",
        ]
class Tipo_ProductoForm(forms.ModelForm):
    class Meta:
        model = Tipo_Producto
        fields = [
            "tipo",
        ]

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = [
            "material",
        ]

class LongitudForm(forms.ModelForm):
    class Meta:
        model = Longitud
        fields = [
            "longitud",
        ]

class CalibreForm(forms.ModelForm):
    class Meta:
        model = Calibre
        fields = [
            "calibre",
        ]

class FormaForm(forms.ModelForm):
    class Meta:
        model = Forma
        fields = [
            "forma",
        ]
