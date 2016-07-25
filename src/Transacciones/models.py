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
    fecha   =    models.DateTimeField()
    Credito_id  = models.ForeignKey('Credito')

    def __unicode__(self):
        return str(self.monto)


class Factura(models.Model):
    serie   =   models.CharField(max_length = 3, blank=True,null=True)
    noDocumento = models.PositiveIntegerField(null = True,blank = True)
    precioTotal = models.FloatField(null = True,blank=True,validators=[MinValueValidator(0)])
    anulada = models.BooleanField( default = False)
    Comodin_id = models.ForeignKey('Comodin.Comodin')

    def __unicode__(self):
        return str(self.noDocumento) + "  "+ self.serie + str(self.Comodin_id)

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
    fechaLimite =   models.DateTimeField()
    fechaAprobacion =    models.DateTimeField()
    Usuario_id  =   models.ForeignKey('Usuario.Usuario')
    Factura_id   = models.ForeignKey('Factura')

    def __unicode__ (self):
        return self.usuario_id + "  "+ self.factura_id


# @receiver(post_save, sender = DetalleFactura)
# def creacionLote(sender, instance, created, *args, **kwargs):
#     if created:
#          NuevoLote = Lote()
#          NuevoLote.cantidad= instance.cantidad
#          NuevoLote.Producto_id = instance.Producto_id
#          NuevoLote.precio_compra = instance.subTotal
#          NuevoLote.save()
