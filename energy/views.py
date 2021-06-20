from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.db.models import Sum
from energy.models import Inverter, Photovoltaic, Radiation

# Create your views here.


def index(request):
    test = Radiation.objects.values('location', 'slope', 'azimuth', 'inverter_model__inverter_model',
                                    'pv_model__facility_name', 'pv_model__pv_model', 'pv_model__number_of_modules')
    search_form1 = HomeFilterSearchRadiation(request.POST)
    search_form2 = HomeFilterSearchPV(request.POST)

    return render(request, 'index.html', {'context': test, 'form_rad': search_form1, 'form_pv': search_form2})


def test_admin(request):
    pvs = Photovoltaic.objects.all()
    inverters = Inverter.objects.all()
    monthrad = Radiation.objects.all()

    context = {'pvs': pvs, 'inverters': inverters, 'monthrad':monthrad}
    return render(request, 'energy/index.html', context)


def add_pv(request):
    if request.method == 'POST':
        form = PvForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = PvForm()
        return render(request, 'energy/add_data.html', {'form': form})


def add_inverter(request):
    if request.method == 'POST':
        form = InverterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = InverterForm()
        return render(request, 'energy/add_data.html', {'form': form})


def add_radiation(request):
    if request.method == 'POST':
        form = RadiationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = RadiationForm()
        return render(request, 'energy/add_data.html', {'form': form})


def edit_pv(request, pk):
    item = get_object_or_404(Photovoltaic, pk=pk)
    if request.method == 'POST':
        form = PvForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = PvForm(instance=item)
        return render(request, 'energy/edit_pv.html', {'form': form})


def delete_pv(request, pk):
    Photovoltaic.objects.filter(id=pk).delete()
    items = Photovoltaic.objects.all()
    context = {
        'items': items
    }

    return render(request, 'energy/index.html', context)


def display_monthlyRad(request):
    mysum = Radiation.objects.values('month') \
        .annotate(radiations=Sum('radiations')) \
        .order_by('month')
    context = {
        'mysum': mysum,
    }

    return render(request, 'energy/monthly_radiation.html', context)



