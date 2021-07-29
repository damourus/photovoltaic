from .models import *
from django import forms


class PvForm(forms.ModelForm):
    class Meta:
        model = Photovoltaic
        fields = ('facility_name', 'pv_model', 'envelope_selection', 'direction', 'number_of_modules',
                  'non_vertical_surface_solar_attenuation_rate', 'total_equipment_cost')


class InverterForm(forms.ModelForm):
    class Meta:
        model = Inverter
        fields = ('inverter_model', )


class RadiationForm(forms.ModelForm):
    class Meta:
        model = Radiation
        fields = ('location', 'azimuth', 'slope')


# class HomeFilterSearchRadiation(forms.ModelForm):
#     class Meta:
#         model = Radiation
#         fields = ('location', 'azimuth', 'slope',)
#
#
# class HomeFilterSearchPV(forms.ModelForm):
#     class Meta:
#         model = Photovoltaic
#         fields = ('facility_name',)


