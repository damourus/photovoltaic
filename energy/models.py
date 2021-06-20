from django.db import models
from django.db.models import Sum

# Create your models here.


# class InverterCategory(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name


class Inverter(models.Model):
    CATEGORY = {
        ('Satcon Technology: PVS-30 (480V) 480V [CEC 2016]', 'Satcon Technology: PVS-30 (480V) 480V [CEC 2016]'),
        ('ABB: MICRO-0.25-I-OUTD-US-208 [208V] 208V [CEC 2018]', 'ABB: MICRO-0.25-I-OUTD-US-208 [208V] 208V [CEC 2018]'),
        ('SMA America: SB7000US 240V [CEC 2007]', 'SMA America: SB7000US 240V [CEC 2007]'),
        ('OPTI International: GT 3000 (208V) 208V [CEC 2016]', 'OPTI International: GT 3000 (208V) 208V [CEC 2016]'),
    }
    # inverter_model = models.ForeignKey(InverterCategory, on_delete=models.CASCADE)
    inverter_model = models.CharField(max_length=200, null=True, choices=CATEGORY)
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
        return self.inverter_model


class Photovoltaic(models.Model):
    choices = {
        ('Yes', 'Yes'),
        ('No', 'No'),
    }
    TYPES ={
        ('Neo Solar Power D6M350E4AME', 'Neo Solar Power D6M350E4AME'),
        ('A10Green Technology A10J-M60-235', 'A10Green Technology A10J-M60-235'),
        ('A10Green Technology A10J-M60-220', 'A10Green Technology A10J-M60-220'),
        ('LG Electronics LG345S2W-A5', 'LG Electronics LG345S2W-A5'),
    }
    facility_name = models.CharField(max_length=8, null=True)
    inverter_model = models.ForeignKey(Inverter, null=True, on_delete=models.CASCADE)
    pv_model = models.CharField(max_length=300, null=True, choices=TYPES)
    rated_power = models.IntegerField(max_length=10, null=True)
    number_of_modules = models.IntegerField(max_length=8, null=True)
    b_i_p_v = models.CharField(max_length=3, null=True, choices=choices)
    width = models.FloatField(max_length=10, null=True)
    length = models.IntegerField(max_length=10, null=True)

    def _area(self):
        return self.width * self.length * self.number_of_modules

    area = property(_area)

    def _efficiency(self):
        return self.rated_power * 100 / self.width / self.length / 1000

    efficiency = property(_efficiency)

    def __str__(self):
        return self.pv_model


class Radiation(models.Model):
    location = models.CharField(max_length=50, null=True)
    slope = models.FloatField(max_length=10, null=True)
    azimuth = models.IntegerField(max_length=10, null=True)
    radiations = models.FloatField(max_length=10, null=True)
    correction_rate = models.FloatField(max_length=10, null=True)
    month = models.CharField(max_length=10, null=True)
    day = models.IntegerField(max_length=10, null=True)
    time = models.TimeField(max_length=10, null=True)
    pv_model = models.ForeignKey(Photovoltaic, max_length=10, null=True, on_delete=models.CASCADE)
    inverter_model = models.ForeignKey(Inverter, max_length=10, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.location

