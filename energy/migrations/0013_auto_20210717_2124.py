# Generated by Django 3.1.7 on 2021-07-17 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0012_auto_20210717_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photovoltaic',
            name='direction',
            field=models.CharField(choices=[('West', 'West'), ('East', 'East'), ('North', 'North'), ('South', 'South')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='photovoltaic',
            name='envelope_selection',
            field=models.CharField(choices=[('North Roof', 'North Roof'), ('West Roof', 'West Roof'), ('East Roof', 'East Roof'), ('South Roof', 'South Roof')], max_length=10, null=True),
        ),
    ]