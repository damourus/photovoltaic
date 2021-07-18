# Generated by Django 3.1.7 on 2021-07-17 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0011_auto_20210717_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photovoltaic',
            name='direction',
            field=models.CharField(choices=[('North', 'North'), ('South', 'South'), ('West', 'West'), ('East', 'East')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='photovoltaic',
            name='envelope_selection',
            field=models.CharField(choices=[('West Roof', 'West Roof'), ('South Roof', 'South Roof'), ('East Roof', 'East Roof'), ('North Roof', 'North Roof')], max_length=10, null=True),
        ),
    ]
