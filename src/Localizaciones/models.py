from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Departamento(models.Model):
    id = models.AutoField(primary_key = True)
    departamento = models.CharField(max_length = 45)

    def __unicode__(self):
        return self.departamento


class Municipio(models.Model):
    id = models.AutoField(primary_key=True)
    municipio = models.CharField(max_length = 45)
    Departamento_id = models.ForeignKey('Departamento')

    def __unicode__(self):
        return self.municipio
