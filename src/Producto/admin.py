from django.contrib import admin
from .models import Lote, Producto, Tipo_Producto,Material, Longitud, Calibre, Forma
from .forms import LoteForm, ProductoForm, Tipo_ProductoForm,MaterialForm, LongitudForm, CalibreForm, FormaForm

class LoteAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "precio_compra",
        "Producto_id",
    ]
    form = LoteForm

class ProductoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "descripcion",
        "Tipo_Producto_id",
        "Material_id",
        "Longitud_id",
        "Calibre_id",
        "Forma_id",
        "Marca_id",
    ]
    form = ProductoForm

class Tipo_ProductoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "tipo",
    ]
    form = Tipo_ProductoForm

class MaterialAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "material",
    ]
    form = MaterialForm

class LongitudAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "longitud",
    ]
    form = LongitudForm

class CalibreAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "calibre",
    ]
    form = CalibreForm

class FormaAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "forma",
    ]
    form = FormaForm

admin.site.register(Lote, LoteAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Tipo_Producto, Tipo_ProductoAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Longitud, LongitudAdmin)
admin.site.register(Calibre, CalibreAdmin)
admin.site.register(Forma, FormaAdmin)
