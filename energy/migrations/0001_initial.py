# Generated by Django 3.1.7 on 2021-06-26 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InverterCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PvCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Radiation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('slope', models.FloatField(max_length=10)),
                ('azimuth', models.IntegerField(max_length=10)),
                ('radiations', models.FloatField(max_length=10)),
                ('correction_rate', models.FloatField(max_length=10)),
                ('month', models.CharField(max_length=10)),
                ('day', models.IntegerField(max_length=10)),
                ('time', models.TimeField(max_length=10)),
                ('inverter_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='energy.invertercategory')),
                ('pv_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='energy.pvcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Photovoltaic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility_name', models.CharField(max_length=8)),
                ('rated_power', models.IntegerField(max_length=10)),
                ('number_of_modules', models.IntegerField(max_length=8)),
                ('b_i_p_v', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], max_length=4)),
                ('width', models.FloatField(max_length=10)),
                ('length', models.IntegerField(max_length=10)),
                ('envelope_selection', models.CharField(choices=[('North Roof', 'North Roof'), ('East Roof', 'East Roof'), ('South Roof', 'South Roof'), ('West Roof', 'West Roof')], max_length=10)),
                ('direction', models.CharField(choices=[('South', 'South'), ('East', 'East'), ('West', 'West'), ('North', 'North')], max_length=10)),
                ('non_vertical_surface_solar_attenuation_rate', models.FloatField(max_length=10)),
                ('total_equipment_cost', models.IntegerField(max_length=10)),
                ('inverter_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='energy.invertercategory')),
                ('pv_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='energy.pvcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Inverter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nominal_ac_voltage', models.IntegerField(max_length=10)),
                ('maximum_ac_power', models.IntegerField(max_length=10)),
                ('maximum_dc_power', models.FloatField(max_length=10)),
                ('nominal_dc_voltage', models.FloatField(max_length=10)),
                ('power_consumption_during_operation', models.FloatField(max_length=10)),
                ('power_consumption_at_night', models.FloatField(max_length=10)),
                ('maximum_dc_voltage', models.IntegerField(max_length=10)),
                ('maximum_dc_current', models.FloatField(max_length=10)),
                ('minimum_mppt_dc_voltage', models.IntegerField(max_length=10)),
                ('maximum_mppt_dc_voltage', models.IntegerField(max_length=10)),
                ('inverter_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='energy.invertercategory')),
            ],
        ),
    ]
