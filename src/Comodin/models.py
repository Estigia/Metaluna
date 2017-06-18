from __future__ import unicode_literals
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models

# Create your models here.

class Comodin(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 45, blank = False, null = True)
    empresa = models.CharField(max_length = 45, blank = False, null = True)
    direccion = models.CharField(max_length = 45, blank = False, null = True)
    telefono = models.CharField(max_length = 8)
    nit = models.CharField(max_length = 20, blank = False, null = True)
    #False: Cliente, True: Proveedor.
    tipo = models.BooleanField()
    bloqueado = models.BooleanField(default = False)
    saldo = models.FloatField(null=True,blank=True,validators=[MinValueValidator(0)])

    municipio = models.ForeignKey('Localizaciones.Municipio')

    def __unicode__(self):
        return self.nombre + "--" + self.empresa

class Marca(models.Model):
    id = models.AutoField(primary_key = True)
    marca = models.CharField(max_length = 45)

    Comodin_id = models.ForeignKey('Comodin')

    def __unicode__(self):
        return str(self.marca)
