# Generated by Django 3.1.7 on 2021-07-27 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0028_auto_20210727_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photovoltaic',
            name='direction',
            field=models.CharField(choices=[('South', 'South'), ('East', 'East'), ('North', 'North'), ('West', 'West')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='photovoltaic',
            name='envelope_selection',
            field=models.CharField(choices=[('West Roof', 'West Roof'), ('East Roof', 'East Roof'), ('South Roof', 'South Roof'), ('North Roof', 'North Roof')], max_length=10, null=True),
        ),
    ]
