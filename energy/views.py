from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.urls import reverse
from .forms import *
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def index(request):
    if request.method == "POST":
        pv_form = PvForm(request.POST)
        inverter_form = InverterForm(request.POST)
        radiation_form = RadiationForm(request.POST)

        if pv_form.is_valid() and inverter_form.is_valid() and radiation_form.is_valid():
            pv = pv_form.save()
            inverter = inverter_form.save(False)
            radiation = radiation_form.save(False)

            inverter.pv = pv
            inverter.save()
            radiation.pv = pv
            radiation.save()

            return redirect(reverse('index'))

    else:
        pv_form = PvForm()
        inverter_form = InverterForm()
        radiation_form = RadiationForm()

    args = {}
    args.update(csrf(request))
    args['pv_form'] = pv_form
    args['inverter_form'] = inverter_form
    args['radiation_form'] = radiation_form

    return render(request, 'energy/index.html', args)


def display_monthlyRad(request):
    mysum = Radiation.objects.values('month') \
        .annotate(m=Sum(F('radiations') * F('correction_rate'))) \
        .order_by('month')
    context = {
        'mysum': mysum,
    }

    return render(request, 'energy/monthly_radiation.html', context)


def energyCall(request):
    items = dict()
    for x in range(12):
        items[x] = energyGeneration(x)

    return render(request, "energy/energy_generated.html", {"items": items})


