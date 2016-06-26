from django.shortcuts import render

from .forms import PlanillaForm

# Create your views here.
def Planilla(request):
    form = PlanillaForm(request.POST or None)
    context = {
        "form":form,
    }

    if form.is_valid():
        form.save()

    return render(request, 'planillas/planilla.html', context)
