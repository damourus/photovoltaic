from django.db import models
from django.db.models import Sum, F

# Create your models here.


class InverterCategory(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class PvCategory(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Inverter(models.Model):
    inverter_model = models.ForeignKey(InverterCategory, on_delete=models.CASCADE)
    nominal_ac_voltage = models.IntegerField(max_length=10, null=True)
    maximum_ac_power = models.IntegerField(max_length=10, null=True)
    maximum_dc_power = models.FloatField(max_length=10, null=True)
    nominal_dc_voltage = models.FloatField(max_length=10, null=True)
    power_consumption_during_operation = models.FloatField(max_length=10, null=True)
    power_consumption_at_night = models.FloatField(max_length=10, null=True)
    maximum_dc_voltage = models.IntegerField(max_length=10, null=True)
    maximum_dc_current = models.FloatField(max_length=10, null=True)
    minimum_mppt_dc_voltage = models.IntegerField(max_length=10, null=True)
    maximum_mppt_dc_voltage = models.IntegerField(max_length=10, null=True)

    def inveff(self):
        return self.maximum_ac_power / self.maximum_dc_power
    inveff = property(inveff)

    def _invertereff(self):
        return self.inveff * 100

    invertereff = property(_invertereff)

    def rloss(self):
        return (1-(1-0.02) * (1-0.03) * (1-0.02) * (1-0.01) * (1-0.015) * (1-0.02) * (1-0.005) * (1-0.03) * self.inveff) * 100

    loss = property(rloss)

    def __str__(self):
        return self.inverter_model.name


class Photovoltaic(models.Model):
    choices = {
        ('Yes', 'Yes'),
        ('No', 'No'),
    }
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
    facility_name = models.CharField(max_length=8, null=True)
    pv_model = models.ForeignKey(PvCategory, null=True, on_delete=models.CASCADE)
    inverter_model = models.ForeignKey(InverterCategory, null=True, on_delete=models.CASCADE)
    rated_power = models.IntegerField(max_length=10, null=True)
    number_of_modules = models.IntegerField(max_length=8, null=True)
    b_i_p_v = models.CharField(max_length=4, null=True, choices=choices)
    width = models.FloatField(max_length=10, null=True)
    length = models.IntegerField(max_length=10, null=True)
    envelope_selection = models.CharField(max_length=10, null=True, choices=TYPES)
    direction = models.CharField(max_length=10, null=True, choices=Choices)
    non_vertical_surface_solar_attenuation_rate = models.FloatField(max_length=10, null=True)
    total_equipment_cost = models.IntegerField(max_length=10, null=True)

    def _area(self):
        return self.width * self.length * self.number_of_modules

    area = property(_area)

    def _efficiency(self):
        return self.rated_power * 100 / self.width / self.length / 1000

    efficiency = property(_efficiency)

    def __str__(self):
        return self.pv_model.name


class Radiation(models.Model):
    location = models.ForeignKey(Location, null=True, on_delete=models.CASCADE)
    slope = models.FloatField(max_length=10, null=True)
    azimuth = models.IntegerField(max_length=10, null=True)
    radiations = models.FloatField(max_length=10, null=True)
    correction_rate = models.FloatField(max_length=10, null=True)
    month = models.CharField(max_length=10, null=True)
    day = models.IntegerField(max_length=10, null=True)
    time = models.TimeField(max_length=10, null=True)

    def monthlyRadiation(self):
        self.mysum = Radiation.objects.values('month') \
            .annotate(m=Sum(F('radiations') * F('correction_rate'))) \
            .order_by('month')

        return self.mysum

    monthlyRadiation = property(monthlyRadiation)

    def __str__(self):
        return f"{self.location.name}  {self.time} {self.day}"


def getCategoryId(n):
    pc = PvCategory.objects.all().get(name=n)
    return pc.id


def comparePvModel(fromForm):
    myid = getCategoryId(fromForm)
    pvname = Photovoltaic.objects.all().get(pv_model_id=myid).pv_model

    return pvname


def getCategoryInvId(n):
    invc = InverterCategory.objects.all().get(name=n)
    return invc.id


def compareInverterModel(fromForm):
    invid = getCategoryId(fromForm)
    invname = Inverter.objects.all().get(inverter_model_id=invid).inverter_model

    return invname


def getLocation(n):
    L = Location.objects.all().get(name=n)
    return L.id


def compareLocation(fromForm):
    locationid = getLocation(fromForm)
    locationname = Radiation.objects.all().get(location_id=locationid).location

    return locationname


def energyGeneration(month, fromForm):
    myid = getCategoryId(fromForm)
    invid = getCategoryId(fromForm)
    locationid = getCategoryId(fromForm)
    pv = Photovoltaic.objects.all().get(pv_model_id=myid)
    inv = Inverter.objects.all().get(inverter_model_id=invid)
    rad = Radiation.objects.all().get(location_id=locationid)
    results = rad.monthlyRadiation[month]['m'] * (pv.efficiency / 100) * (1-pv.non_vertical_surface_solar_attenuation_rate) * (1-(inv.loss /100)) * pv.area

    return results



