from .models import *
from django import forms


class PvForm(forms.ModelForm):
    class Meta:
        model = Photovoltaic
        fields = ('pv_model', )


class InverterForm(forms.ModelForm):
    class Meta:
        model = Inverter
        fields = ('inverter_model', )


class RadiationForm(forms.ModelForm):
    class Meta:
        model = Radiation
        fields = ('location', 'azimuth', 'slope')


class InputForm(forms.Form):

    TYPES = {
        ('South Roof', 'South Roof'),
        ('North Roof', 'North Roof'),
        ('West Roof', 'West Roof'),
        ('East Roof', 'East Roof'),
    }
    Choices = {
        ('South', 'South'),
        ('North', 'North'),
        ('West', 'West'),
        ('East', 'East'),
    }

    facility_name = forms.CharField(label = 'Facility Name', max_length=10)
    envelope_selection = forms.ChoiceField(label = 'Envelope Selection', choices=TYPES)
    direction = forms.ChoiceField(label = 'Direction', choices=Choices)
    number_of_modules = forms.IntegerField(label = 'Number of Modules (EA)')
    non_vertical_surface_solar_attenuation_rate = forms.FloatField(label = 'Non-Vertical Surface Solar Attenuation Rate')
    total_equipment_cost = forms.IntegerField(label = 'Total Equipment Cost')


