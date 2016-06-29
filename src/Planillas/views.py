from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from .forms import PlanillaForm

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
