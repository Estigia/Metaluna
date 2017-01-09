from __future__ import unicode_literals
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models

# Create your models here.

class Agencia(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 30, blank = True, null = True)
    direccion = models.CharField(max_length = 45)
    capital = models.FloatField(null=True,blank=True,validators=[MinValueValidator(0)])
    Municipio_id = models.ForeignKey('Localizaciones.Municipio')

    def __unicode__(self):
        return self.nombre


class Vehiculo(models.Model):
    id = models.AutoField(primary_key = True)
    marca = models.CharField(max_length = 20, blank = True, null = True)
    modelo = models.IntegerField(blank = True, null = True)
    placa = models.CharField(max_length = 7, blank = True, null = True)
    Agencia_id = models.ForeignKey('Agencia')

    def __unicode__(self):
        return self.placa


class Entrega(models.Model):
    id = models.AutoField(primary_key = True)
    kEntrada = models.FloatField()
    kSalida = models.FloatField()
    fecha = models.DateTimeField()
    vale = models.IntegerField(blank = True, null = True)
    Vehiculo_id = models.ForeignKey('Vehiculo')

    def __unicode__(self):
        return str(self.id)

    def kTotal(self):
        return self.kEntrada - self.kSalida


class Mercaderia(models.Model):
    id = models.AutoField(primary_key = True)
    Producto_id = models.ForeignKey('Producto.Producto')
    Agencia_id = models.ForeignKey('Agencia')
    cantidad = models.IntegerField(blank = True, null = True)

    def __unicode__(self):
        return str(self.Producto_id)
