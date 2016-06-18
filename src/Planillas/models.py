from __future__ import unicode_literals
from django.db import models

from django.core.validators import MinValueValidator



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