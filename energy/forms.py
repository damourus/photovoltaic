from django import forms
from .models import *


class PvForm(forms.ModelForm):
    class Meta:
        model = Photovoltaic
        fields = '__all__'


class InverterForm(forms.ModelForm):
    class Meta:
        model = Inverter
        fields = ('inverter_model', 'nominal_ac_voltage', 'maximum_ac_power', 'maximum_dc_power', 'nominal_dc_voltage',
                  'power_consumption_during_operation', 'power_consumption_at_night', 'maximum_dc_voltage',
                  'maximum_dc_current', 'minimum_mppt_dc_voltage', 'maximum_mppt_dc_voltage')


class RadiationForm(forms.ModelForm):
    class Meta:
        model = Radiation
        fields = '__all__'

