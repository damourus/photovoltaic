from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf
from django.urls import reverse
from .forms import *
from django.db.models import Sum
from energy.models import *

# Create your views here.


# def index(request):
#     test = Radiation.objects.values('location', 'slope', 'azimuth', 'inverter_model__inverter_model__name',
#                                     'pv_model__facility_name', 'pv_model__pv_model__name', 'pv_model__number_of_modules')
#     search_form1 = HomeFilterSearchRadiation(request.POST)
#     search_form2 = HomeFilterSearchPV(request.POST)
#
#     return render(request, 'index.html', {'context': test, 'form_rad': search_form1, 'form_pv': search_form2})


def index(request):
    pvs = Photovoltaic.objects.all()
    inverters = Inverter.objects.all()
    monthrad = Radiation.objects.all()

    mysum = Radiation.objects.values('month') \
    .annotate(radiations=Sum('radiations')) \
        .order_by('month')

    context = {'pvs': pvs, 'inverters': inverters, 'monthrad': monthrad, 'mysum': mysum}
    return render(request, 'energy/index.html', context)


def add_data(request):
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

    return render(request, 'energy/add_data.html', args)



# def add_pv(request):
#     if request.method == 'POST':
#         form = PvForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#     else:
#         form = PvForm()
#         return render(request, 'energy/add_data.html', {'form': form})
#
#
# def add_inverter(request):
#     if request.method == 'POST':
#         form = InverterForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#     else:
#         form = InverterForm()
#         return render(request, 'energy/add_data.html', {'form': form})
#
#
# def add_radiation(request):
#     if request.method == 'POST':
#         form = RadiationForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#     else:
#         form = RadiationForm()
#         return render(request, 'energy/add_data.html', {'form': form})


# def edit_pv(request, pk):
#     item = get_object_or_404(Photovoltaic, pk=pk)
#     if request.method == 'POST':
#         form = PvForm(request.POST, instance=item)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#     else:
#         form = PvForm(instance=item)
#         return render(request, 'energy/edit_pv.html', {'form': form})
#
#
# def delete_pv(request, pk):
#     Photovoltaic.objects.filter(id=pk).delete()
#     items = Photovoltaic.objects.all()
#     context = {
#         'items': items
#     }
#
#     return render(request, 'energy/index.html', context)
#
#
# def display_monthlyRad(request):
#     mysum = Radiation.objects.values('month') \
#         .annotate(radiations=Sum('radiations')) \
#         .order_by('month')
#     context = {
#         'mysum': mysum,
#     }
#
#     return render(request, 'energy/monthly_radiation.html', context)



