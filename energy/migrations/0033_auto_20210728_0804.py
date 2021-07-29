# Generated by Django 3.1.7 on 2021-07-28 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0032_auto_20210728_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photovoltaic',
            name='b_i_p_v',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='photovoltaic',
            name='direction',
            field=models.CharField(choices=[('South', 'South'), ('East', 'East'), ('West', 'West'), ('North', 'North')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='photovoltaic',
            name='envelope_selection',
            field=models.CharField(choices=[('West Roof', 'West Roof'), ('North Roof', 'North Roof'), ('East Roof', 'East Roof'), ('South Roof', 'South Roof')], max_length=10, null=True),
        ),
    ]
