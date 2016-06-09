from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Recibo(models.Model):
    noDocumento = models.PositiveIntegerField(null=False,blank=False)
    def __unicode__(self):
        return self.noDocumento

class Abonos(models.Model):
    monto   =  models.PositiveIntegerField(null=False,blank=False)
    fecha   =    models.DateTimeField()
    credito_id  = models.ForeignKey('Credito')

    def __unicode__(self):
        return self.monto


class Factura(models.Model):
    serie   =   models.CharField(max_length = 3, blank=False,null=False)
    noDocumento = models.PositiveIntegerField(null = False,blank = False)
    precioTotal = models.PositiveIntegerField(null = False,blank=False)
    anulada = models.BooleanField( default = False)
    Comodin_id = models.ForeignKey('Usuario.Comodin')

    def __unicode__(self):
        return self.noDocumento + "  "+ self.serie

class DetalleFactura(models.Model):
    Factura_id = models.ForeignKey('Factura')
    Producto_id = models.ForeignKey('Producto.Producto')
    subTotal = models.PositiveIntegerField(null = False,blank=False)
    cantidad = models.PositiveIntegerField(null = False,blank=False)
    def __unicode__(self):
        return self.subTotal



class Credito(models.Model):
    aprobado    =   models.BooleanField(default = True)
    monto   =   models.PositiveIntegerField(null = False,blank=False)
    saldo   =   models.PositiveIntegerField(null = False,blank=False)
    finalizado  =   models.BooleanField(default=True)
    fechaLimite =   models.DateTimeField()
    fechaAprobacion =    models.DateTimeField()
    usuario_id  =   models.ForeignKey('Usuarios.Usuario')
    factura_id   = models.ForeignKey('Factura')

    def __unicode__ (self):
        return self.monto + "  "+ self.saldo
