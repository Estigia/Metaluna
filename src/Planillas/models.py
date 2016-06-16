from __future__ import unicode_literals
from django.db import models

from django.core.validators import MinValueValidator



# Create your models here.
class Planilla(models.Model):

    sueldo = models.FloatField(blank = False, null = False)
    horasExtra = models.FloatField(blank = False, null = False)
    bonoIncentivo = models.FloatField(blank = False, null = False)
    #descuentos
    igss = models.FloatField(blank = False, null = False)
    isr = models.FloatField(blank = False, null = False)
    anticipos = models.FloatField(blank = False, null = False)
    judiciales = models.FloatField(blank = False, null = False)
    otros = models.FloatField(blank = False, null = False)
    totalDescuento = models.FloatField(blank = False, null = False)
    totalLiquido = models.FloatField(blank = False, null = False)
    Empleado_id = models.ForeignKey('Usuario.Empleado')
    Agencia_id = models.ForeignKey('Agencia.Agencia',default = 1)
    def __unicode__(self):
        return self.totalLiquido
