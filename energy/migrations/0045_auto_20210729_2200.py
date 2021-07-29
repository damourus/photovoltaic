# Generated by Django 3.1.7 on 2021-07-29 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0044_auto_20210729_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photovoltaic',
            name='direction',
            field=models.CharField(choices=[('North', 'North'), ('East', 'East'), ('West', 'West'), ('South', 'South')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='photovoltaic',
            name='envelope_selection',
            field=models.CharField(choices=[('West Roof', 'West Roof'), ('East Roof', 'East Roof'), ('South Roof', 'South Roof'), ('North Roof', 'North Roof')], max_length=10, null=True),
        ),
    ]