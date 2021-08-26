from django.db import models


# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class InverterCategory(models.Model):
    name = models.CharField(max_length=300, null=False)

    def __str__(self):
        return self.name


class PvCategory(models.Model):
    name = models.CharField(max_length=300, null=False)

    def __str__(self):
        return self.name


class Photovoltaic(models.Model):
    pv_model = models.ForeignKey(PvCategory, null=False, on_delete=models.CASCADE)
    rated_power = models.IntegerField(max_length=10, null=True)
    b_i_p_v = models.CharField(max_length=4, null=False)
    width = models.FloatField(max_length=10, null=False)
    length = models.IntegerField(max_length=10, null=False)

    @property
    def area(self):
        return self.width * self.length

    @property
    def efficiency(self):
        return self.rated_power * 100 / self.width / self.length / 1000

    def __str__(self):
        return self.pv_model.name


class Inverter(models.Model):
    inverter_model = models.ForeignKey(InverterCategory, on_delete=models.CASCADE)
    nominal_ac_voltage = models.IntegerField(max_length=10, null=False)
    maximum_ac_power = models.IntegerField(max_length=10, null=False)
    maximum_dc_power = models.FloatField(max_length=10, null=False)
    nominal_dc_voltage = models.FloatField(max_length=10, null=False)
    power_consumption_during_operation = models.FloatField(max_length=10, null=False)
    power_consumption_at_night = models.FloatField(max_length=10, null=False)
    maximum_dc_voltage = models.IntegerField(max_length=10, null=False)
    maximum_dc_current = models.FloatField(max_length=10, null=False)
    minimum_mppt_dc_voltage = models.IntegerField(max_length=10, null=False)
    maximum_mppt_dc_voltage = models.IntegerField(max_length=10, null=False)

    @property
    def inveff(self):
        return self.maximum_ac_power / self.maximum_dc_power

    @property
    def invertereff(self):
        return self.inveff * 100

    @property
    def rloss(self):
        return (1-(1-0.02) * (1-0.03) * (1-0.02) * (1-0.01) * (1-0.015) * (1-0.02) * (1-0.005) * (1-0.03) * self.inveff) * 100

    def __str__(self):
        return self.inverter_model.name


class Radiation(models.Model):
    location = models.ForeignKey(Location, null=True, on_delete=models.CASCADE)
    slope = models.FloatField(max_length=10, null=True)
    azimuth = models.IntegerField(max_length=10, null=True)
    radiations = models.FloatField(max_length=10, null=True)
    correction_rate = models.FloatField(max_length=10, null=True)
    month = models.IntegerField(max_length=10, null=True)
    day = models.IntegerField(max_length=10, null=True)
    time = models.IntegerField(max_length=10, null=True)

    def __str__(self):
        return f"{self.location.name}  {self.time} {self.day}"






