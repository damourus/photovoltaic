# Generated by Django 3.1.7 on 2021-07-18 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0014_auto_20210717_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photovoltaic',
            name='direction',
            field=models.CharField(choices=[('East', 'East'), ('West', 'West'), ('North', 'North'), ('South', 'South')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='photovoltaic',
            name='envelope_selection',
            field=models.CharField(choices=[('West Roof', 'West Roof'), ('East Roof', 'East Roof'), ('North Roof', 'North Roof'), ('South Roof', 'South Roof')], max_length=10, null=True),
        ),
    ]
