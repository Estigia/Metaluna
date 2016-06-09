from __future__ import unicode_literals
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser

from django.db import models

# Create your models here.

class Puesto(models.Model):
    id = models.AutoField(primary_key = True)
    puesto = modesl.CharField(max_length = 45)

class Tipo_Usuario(models.Model):
    id = models.AutoField(primary_key = True)
    tipo = models.CharField(max_length = 45)

    def __unicode__(self):
        return str(self.tipo)

class Empleado(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 55, blank = False, null = True)
    apellidos = models.CharField(max_length = 90, blank = False, null = True)
    cui = models.CharField(max_length = 13, blank = False, null = True)
    nit = models.CharField(max_length = 20, blank = False, null = True)
    sueldo = models.DecimalField(decimal_places = 2, blank = False, null = True)

    Puesto_id = models.ForeignKey('Puesto')
    Agencia_id = models.ForeignKey('Agencia.agencia')

    REQUIRED_FIELDS = ['nombre', 'apellidos', 'cui', 'nit', 'sueldo']

    def __unicode__(self):
        return str(nombre) + str(apellidos)

class Comodin(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 45, blank = False, null = True)
    empresa = models.CharField(max_length = 45, blank = False, null = True)
    direccion = models.CharField(max_length = 45, blank = False, null = True)
    telefono = models.CharField(max_length = 8)
    nit = models.CharField(max_length = 20, blank = False, null = True)
    tipo = models.BooleanField(default = False)
    bloqueado = models.BooleanField(default = False)
    saldo = modesl.DecimalField(decimal_places = 2, blank = False, null = True)

    def __unicode__(self):
        return str(self.nombre) + "--" + str(self.empresa)


class UsuarioManager(BaseUserManager):

    def create_user(self, username, Empleado_id, password=None):
		if not username:
			raise ValueError('Ingrese un nombre de usuario valido.')
        if not Empleado_id:
            raise ValueError('Ingrese un Empleado_id')

		usuario = self.model(
				username = nombre_usuario,
                Empleado_id = Empleado_id,
			)

	 	usuario.set_password(password)
	 	usuario.save()

	 	return usuario

	def create_superuser(self, username, Empleado_id, password=None):
	 	usuario = self.create_user(username, Empleado_id, password)
	 	usuario.is_admin = True
	 	usuario.save()

	 	return usuario


class Usuario(AbstractBaseUser):
    id = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 45)
    is_staff = models.BooleanField(default = True)
	is_active = models.BooleanField(default = True)
    ultima_conexion = models.DateTimeField(auto_now_add=False, auto_now=True)

    Tipo_Usuario_id = models.ForeignKey('Tipo_Usuario', default = 1)
    Empleado_id = models.ForeignKey('Empleado')

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'

    def get_full_name(self):
		return str(self.Empleado_id.nombre) + str(self.Empleado_id.apellidos)

	def get_short_name(self):
		return str(self.Empleado_id.nombre)

	def __unicode__(self):
		return self.username

	def has_module_perms(self,perm_list):
		return True

	def has_perm(self,perm):
		return True
