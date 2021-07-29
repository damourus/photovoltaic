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
            pv = pv_form.save(commit=False)
            inverter = inverter_form.save(commit=False)
            radiation = radiation_form.save(commit=False)

            pvFromForm = pv.pv_model
            invFromForm = inverter.inverter_model
            locationFromForm = radiation.location

            energyGenerated = energyGeneration(pvFromForm, invFromForm, locationFromForm)

            return render(request,'energy/energy_generated.html', {'energyGenerated': energyGenerated})

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


def monthlyRadiation3():
    mysum4 = Radiation.objects.values('month') \
        .annotate(m=Sum(F('radiations') * F('correction_rate'))) \
        .order_by('month')
    return mysum4


def getCategoryId(n):
    pc = PvCategory.objects.all().get(name=n)
    return pc.id


def getCategoryInvId(n):
    invc = InverterCategory.objects.all().get(name=n)
    return invc.id


def getLocation(n):
    L = Location.objects.all().get(name=n)
    return L.id


def energyGeneration(pvidFromForm, invidFromForm, locationidFromForm):
    pv = Photovoltaic.objects.all().get(pv_model_id=pvidFromForm)
    inv = Inverter.objects.all().get(inverter_model_id=invidFromForm)
    # rad = Radiation.objects.all().get(location_id=locationidFromForm)
    partialEnergy = (pv.efficiency / 100) * (1 - pv.non_vertical_surface_solar_attenuation_rate) * (
                1 - (inv.rloss / 100)) * pv.area
    allMonthlyRadiations = monthlyRadiation3()
    energyGenerated = []
    for item in allMonthlyRadiations:
        monthlyEnergy = item['m'] * partialEnergy
        monthlyRecord = {'Month': int(item['month']), 'MonthlyEnergy': monthlyEnergy, 'FacilityName': pv.facility_name}
        energyGenerated.append(monthlyRecord)

    return energyGenerated

# def energyCall(request):
#     items = dict()
#     for x in range(12):
#         items[x] = energyGeneration(x)
#
#     return render(request, "energy/energy_generated.html", {"items": items})
#
#
# def test_input(request):
#     pvs = Photovoltaic.objects.all()
#     inverters = Inverter.objects.all()
#     rad = Radiation.objects.all()
#
#     context = {'pvs': pvs, 'inverters': inverters, 'rad': rad}
#
#     return render(request, 'energy/energy_generated.html', context)
