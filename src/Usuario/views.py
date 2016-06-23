from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect

from .models import Empleado
from .forms import InicioForm, UserCreationForm

class EmpleadoCreate(CreateView):
    model = Empleado
    template_name = 'empleado_create.html'

    fields = [
        'nombre',
        'apellidos',
        'cui',
        'nit',
        'sueldo',
        'Puesto_id',
        'Agencia_id',
    ]

def inicio(request):
    if request.user.is_authenticated():

        return render(request,'login.html',{})

    if request.POST:

        form = InicioForm(request.POST or None)

        if form.is_valid():

            username = request.POST['usuario']
            password = request.POST['password']

            user = authenticate(username = username, password = password)

            if user is not None:
                if user.is_active:

                    login(request, user)

                    context = {
                        "form": form,
                    }

                    if request.GET:
                        if request.GET['next'] != '/logout':
                            return HttpResponseRedirect(request.GET['next'])

                    return redirect('/admin')

                else:
                    return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/')
    else:
        form = InicioForm()

        context = {
            'form': form
        }

        return render(request, 'inicio.html', context)

def registro(request):

    if not request.user.is_authenticated():

        form = UserCreationForm(request.POST or None)

        context = {
            "form": form
        }

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/inicio')

        return render(request,'usuario_create.html',context)

    return HttpResponseRedirect('/')
