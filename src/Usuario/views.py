from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

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

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(EmpleadoCreate, self).dispatch(request, *args, **kwargs)

class EmpleadoUpdate(UpdateView):
    model = Empleado
    template_name = 'usuario/empleado_create.html'
    success_url = reverse_lazy('Usuario:empleadoList')

    fields = [
        'nombre',
        'apellidos',
        'cui',
        'nit',
        'sueldo',
        'Puesto_id',
        'Agencia_id'
    ]

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(EmpleadoUpdate, self).dispatch(request, *args, **kwargs)

@login_required(login_url='base')
def empleadoList(request):

    context = {'Empleados':Empleado.objects.all()}

    return render(request, 'usuario/empleados_list.html', context)

class EmpleadoDetail(DetailView):
    model = Empleado
    template_name = 'usuario/empleado_detail.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(EmpleadoDetail, self).dispatch(request, *args, **kwargs)


def inicio(request):
    if request.user.is_authenticated():

        return render(request,'usuario/login.html',{})

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

                    return redirect('/')

                else:
                    return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/')
    else:
        form = InicioForm()

        context = {
            'form': form
        }

        return render(request, 'usuario/inicio.html', context)

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

def homepage(request):
    return render_to_response('usuario/inicio.html')
