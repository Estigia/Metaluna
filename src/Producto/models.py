from __future__ import unicode_literals

from django.db import models

class Lote(models.Model):
    id = models.AutoField(primary_key = True)
    precio_compra = models.FloatField(blank = True, null=True)
    Producto_id = ForeignKey('Producto')

class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField(max_length = 60)
    Tipo_Producto_id = ForeignKey('Tipo_Producto')
    Material_id = ForeignKey('Material')
    Longitud_id = ForeignKey('Longitud')
    Calibre_id = ForeignKey('Calibre')
    Forma_id = ForeignKey('Forma')
    Marca_id = ForeignKey('Comodin.Marca')

class Tipo_Producto(models.Model):
    id = models.AutoField(primary_key = True)
    tipo = models.CharField(max_length = 45, blank = True, null = True)

class Material(models.Model):
    id = models.AutoField(primary_key = True)
    material = models.CharField(max_length = 45, blank = True, null = True)

class Longitud(models.Model):
    id = models.AutoField(primary_key = True)
    longitud = models.IntegerField(blank = True, null = True)

class Calibre(models.Model):
    id = models.AutoField(primary_key = True)
    calibre = models.FloatField(blank = True, null = True)

class Forma(models.Model):
    id = models.AutoField(primary_key = True)
    forma = models.CharField(max_length = 55, blank = True, null = True)
