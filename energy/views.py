from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.urls import reverse
from .forms import *
from django.db.models import Sum, F
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
input = InputForm()

@csrf_exempt
def index(request):
    if request.method == "POST":
        pv_form = PvForm(request.POST)
        inverter_form = InverterForm(request.POST)
        radiation_form = RadiationForm(request.POST)
        input_form = InputForm(request.POST)

        if pv_form.is_valid() and inverter_form.is_valid() and radiation_form.is_valid() and input_form.is_valid():
            pv = pv_form.save(commit=False)
            inverter = inverter_form.save(commit=False)
            radiation = radiation_form.save(commit=False)
            facility_name = input_form.cleaned_data['facility_name']
            number_of_modules = input_form.cleaned_data['number_of_modules']
            non_vertical_surface_solar_attenuation_rate = input_form.cleaned_data['non_vertical_surface_solar_attenuation_rate']

            print (facility_name, number_of_modules, non_vertical_surface_solar_attenuation_rate)


            pvFromForm = pv.pv_model
            invFromForm = inverter.inverter_model
            locationFromForm = radiation.location



            energyGenerated = energyGeneration(pvFromForm, invFromForm, locationFromForm, non_vertical_surface_solar_attenuation_rate, number_of_modules, facility_name)

            return render(request,'energy/energy_generated.html', {'energyGenerated': energyGenerated})

    else:
        pv_form = PvForm()
        inverter_form = InverterForm()
        radiation_form = RadiationForm()
        input_form =InputForm()

    args = {}
    args.update(csrf(request))
    args['pv_form'] = pv_form
    args['inverter_form'] = inverter_form
    args['radiation_form'] = radiation_form
    args['input_form'] =input_form

    return render(request, 'energy/index.html', args)


def monthlyRadiation3():
    mysum4 = Radiation.objects.values('month') \
        .annotate(m=Sum(F('radiations') * F('correction_rate'))) \
        .order_by('month')
    return mysum4


def energyGeneration(pvidFromForm, invidFromForm, locationidFromForm, non_vertical_surface_solar_attenuation_rate, number_of_modules, facility_name):
    pv = Photovoltaic.objects.all().get(pv_model_id=pvidFromForm)
    inv = Inverter.objects.all().get(inverter_model_id=invidFromForm)
    partialEnergy = (pv.efficiency / 100) * (1 - non_vertical_surface_solar_attenuation_rate) * (
            1 - (inv.rloss / 100)) * (pv.area*number_of_modules)
    allMonthlyRadiations = monthlyRadiation3()
    energyGenerated = []
    for item in allMonthlyRadiations:
        monthlyEnergy = item['m'] * partialEnergy
        monthlyRecord = {'Month': int(item['month']), 'MonthlyEnergy': monthlyEnergy, 'FacilityName': facility_name}
        energyGenerated.append(monthlyRecord)

    return energyGenerated

# Following are for Chart to analyse
# def index(request):
#     labels =[] #for horizontal
#     data =[] #for vertical
#
#     queryset =  monthlyRecord.objects.order_by('-month')[:12]
#     for pv in queryset:
#         labels.append(pv.month)
#         data.append(pv.facility_name)
#     return render(request, 'energy/energy_generated.html', {'labels':labels, 'data':data})
