#encoding: utf-8

from django import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import (
                            ReadOnlyPasswordHashField,
                            UserCreationForm,
                            AuthenticationForm
                            )
from django.contrib import messages

from .models import Usuario
from django.contrib.auth import (authenticate,get_user_model,login,logout)


class UserCreationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password1 = forms.CharField(label='Confirmar Password', widget=forms.PasswordInput())

    class Meta:
        model = Usuario
        fields = [
            'username',
            'is_staff'
        ]

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password and password1 and password != password1:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        if password and password1 and len(password) < 8:
            raise forms.ValidationError("Ingrese una contraseña mas larga.")

        return password1

    def save(self, commit = True):
        user = super(UserCreationForm, self).save(commit = False)
        user.set_password(self.cleaned_data.get('password1'))

        if commit:
            user.save()

        return user

class UserChangeForm(forms.Form):

    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password1 = forms.CharField(label='Confirmar password', widget=forms.PasswordInput())

    def clean_password1(self):

        password = self.cleaned_data.get("password")
        password = self.cleaned_data.get("password1")

        if password and password1 and password != password1:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        if password and password1 and len(password) < 8:
            raise forms.ValidationError("Ingrese una contraseña mas larga.")

        return password1

class InicioForm(forms.Form):
    usuario = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    

    # def clean(self, *args, **kwargs):
    #     username = self.cleaned_data.get("username")
    #     password = self.cleaned_data.get("password")
    #     user = authenticate(username=username , password=password)
    #     if not user:
    #         raise forms.ValidationError("Este Usuario no existe")
    #     return super(InicioForm,self).clean(*args,**kwargs)
