from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from Agencia.models import Mercaderia



class Lote(models.Model):
    id = models.AutoField(primary_key = True)
    precio_compra = models.FloatField(null=True,blank=True,validators=[MinValueValidator(0)])
    cantidad = models.IntegerField(blank = True, null = True)
    Producto_id = models.ForeignKey('Producto')
    Agencia_id = models.ForeignKey('Agencia.Agencia')

    def __unicode__(self):
        return str(self.id)

class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField(max_length = 60)
    Tipo_Producto_id = models.ForeignKey('Tipo_Producto')
    Material_id = models.ForeignKey('Material')
    Longitud_id = models.ForeignKey('Longitud')
    Calibre_id = models.ForeignKey('Calibre')
    Forma_id = models.ForeignKey('Forma')
    Marca_id = models.ForeignKey('Comodin.Marca')

    def __unicode__(self):
        return self.descripcion

    def getTotal(self):
        mercaderia = Mercaderia.objects.filter(Producto_id=self)

        total = 0
        for merca in mercaderia:
            total += merca.cantidad

        return total

        
class Tipo_Producto(models.Model):
    id = models.AutoField(primary_key = True)
    tipo = models.CharField(max_length = 45, blank = True, null = True)

    def __unicode__(self):
        return self.tipo

class Material(models.Model):
    id = models.AutoField(primary_key = True)
    material = models.CharField(max_length = 45, blank = True, null = True)

    def __unicode__(self):
        return self.material

class Longitud(models.Model):
    id = models.AutoField(primary_key = True)
    longitud = models.FloatField(null=True,blank=True,validators=[MinValueValidator(0)])

    def __unicode__(self):
        return str(self.longitud)

class Calibre(models.Model):
    id = models.AutoField(primary_key = True)
    calibre = models.FloatField(null=True,blank=True,validators=[MinValueValidator(0)])

    def __unicode__(self):
        return str(self.calibre)

class Forma(models.Model):
    id = models.AutoField(primary_key = True)
    forma = models.CharField(max_length = 55, blank = True, null = True)

    def __unicode__(self):
        return self.forma
