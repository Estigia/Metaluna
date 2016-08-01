from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator

from Producto.models import  Lote

# Create your models here.
class Recibo(models.Model):
    noDocumento = models.PositiveIntegerField(null=True,blank=True)
    def __unicode__(self):
        return str(self.noDocumento)

class Abonos(models.Model):
    monto   =  models.FloatField(null=True,blank=True,validators=[MinValueValidator(0)])
    fecha   =    models.DateTimeField(auto_now_add=False, auto_now=True)
    Credito_id  = models.ForeignKey('Credito')

    def __unicode__(self):
        return str(self.monto)


class Factura(models.Model):
    serie   =   models.CharField(max_length = 3, blank=True,null=True)
    noDocumento = models.PositiveIntegerField(null = True,blank = True)
    precioTotal = models.FloatField(null = True,blank=True,validators=[MinValueValidator(0)])
    anulada = models.BooleanField(default = False)
    fecha = models.DateField(auto_now_add=False, auto_now = True)

    Comodin_id = models.ForeignKey('Comodin.Comodin')

    def __unicode__(self):
        return str(self.noDocumento) + "  "+ self.serie

    def nombre_factura(self):
        return str(self.serie) + str(self.noDocumento)

    class Meta:
        ordering =['-fecha']

class DetalleFactura(models.Model):
    Factura_id = models.ForeignKey('Factura')
    Producto_id = models.ForeignKey('Producto.Producto')
    subTotal = models.FloatField(null = True,blank=True,validators=[MinValueValidator(0)])
    cantidad = models.IntegerField(null = True,blank=True,validators=[MinValueValidator(0)])

    def __unicode__(self):
        return str(self.Factura_id)+'--'+str(self.Producto_id)

    def precioUnitario(self):
        return self.subTotal/self.cantidad



class Credito(models.Model):
    aprobado    =   models.BooleanField(default = True)
    monto   =   models.FloatField(null = True,blank=True,validators=[MinValueValidator(0)])
    saldo   =   models.FloatField(null = True,blank=True,validators=[MinValueValidator(0)])
    finalizado  =   models.BooleanField(default=False)
    fechaLimite =   models.DateField()
    fechaAprobacion =    models.DateField()
    Usuario_id  =   models.ForeignKey('Usuario.Usuario')
    Factura_id   = models.ForeignKey('Factura')

    def __unicode__ (self):
        return str(self.Usuario_id) + "  " + str(self.Factura_id)

    def credito_name(self):
        return str(self.Factura_id)+"--"+str(self.Factura_id.Comodin_id)
