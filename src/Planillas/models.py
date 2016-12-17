from __future__ import unicode_literals
from django.db import models

from django.core.validators import MinValueValidator
from django.utils import timezone



# Create your models here.
class Planilla(models.Model):
    sueldo = models.FloatField(blank = True, null = True)
    horasExtra = models.FloatField(blank = True, null = True)
    bonoIncentivo = models.FloatField(blank = True, null = True)
    #descuentos
    igss = models.FloatField(blank = True, null = True)
    isr = models.FloatField(blank = True, null = True)
    anticipos = models.FloatField(blank = True, null = True)
    judiciales = models.FloatField(blank = True, null = True)
    otros = models.FloatField(blank = True, null = True)
    totalDescuento = models.FloatField(blank = True, null = True)
    totalLiquido = models.FloatField(blank = True, null = True)
    Empleado_id = models.ForeignKey('Usuario.Empleado')
    Agencia_id = models.ForeignKey('Agencia.Agencia',default = 1)
    def __unicode__(self):
        return self.totalLiquido

class Finanzas(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField(max_length = 100, blank = False, null = False)
    #fecha = models.DateField(default = timezone.now()) 
    fecha = models.DateField(auto_now_add=False, auto_now=True)
    #True = ingreso False = egreso
    tipo = models.BooleanField(default = None)
    monto = models.FloatField(blank = False, null = False)
