from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect

from Agencia.models import Agencia
from .forms import PlanillaForm, FinanzasForm
from .models import Finanzas

# Create your views here.
@login_required(login_url='base')
def Planilla(request):
    form = PlanillaForm(request.POST or None)
    context = {
        "form":form,
    }

    if form.is_valid():
        form.save()

    return render(request, 'planillas/planilla.html', context)

@login_required(login_url='base')
def finanzas(request):

    agencias = Agencia.objects.all()
    capital_total = 0
    for agencia in agencias:
        capital_total += agencia.capital

    transacciones = Finanzas.objects.all()

    utilidad = capital_total
    for transaccion in transacciones:
        if transaccion.tipo:
            utilidad += transaccion.monto
        else:
            utilidad -= transaccion.monto

    form = FinanzasForm(request.POST or None)
    context = {
        "form": form,
        "utilidad": utilidad,
        "capital": capital_total,
        "transacciones": Finanzas.objects.all().order_by('-id')[:5]
    }

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/finanzas')

    return render(request, 'planillas/finanzas.html', context)
