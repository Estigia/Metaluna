from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Recibo(models.Model):
    noDocumento = models.PositiveIntegerField(null=True,blank=True)
    def __unicode__(self):
        return str(self.noDocumento)

class Abonos(models.Model):
    monto   =  models.PositiveIntegerField(null=True,blank=True)
    fecha   =    models.DateTimeField()
    Credito_id  = models.ForeignKey('Credito')

    def __unicode__(self):
        return str(self.monto)


class Factura(models.Model):
    serie   =   models.CharField(max_length = 3, blank=True,null=True)
    noDocumento = models.PositiveIntegerField(null = True,blank = True)
    precioTotal = models.PositiveIntegerField(null = True,blank=True)
    anulada = models.BooleanField( default = False)
    Comodin_id = models.ForeignKey('Comodin.Comodin')

    def __unicode__(self):
        return str(self.noDocumento) + "  "+ self.serie + str(self.Comodin_id)

class DetalleFactura(models.Model):
    Factura_id = models.ForeignKey('Factura')
    Producto_id = models.ForeignKey('Producto.Producto')
    subTotal = models.PositiveIntegerField(null = True,blank=True)
    cantidad = models.PositiveIntegerField(null = True,blank=True)

    def __unicode__(self):
        return str(self.Factura_id)+'--'+str(self.Producto_id)

    def precioUnitario(self):
        return self.subTotal/self.cantidad



class Credito(models.Model):
    aprobado    =   models.BooleanField(default = True)
    monto   =   models.PositiveIntegerField(null = True,blank=True)
    saldo   =   models.PositiveIntegerField(null = True,blank=True)
    finalizado  =   models.BooleanField(default=False)
    fechaLimite =   models.DateTimeField()
    fechaAprobacion =    models.DateTimeField()
    Usuario_id  =   models.ForeignKey('Usuario.Usuario')
    Factura_id   = models.ForeignKey('Factura')

    def __unicode__ (self):
        return str(self.Usuario_id) + "  " + str(self.Factura_id)
