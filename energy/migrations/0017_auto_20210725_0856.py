# Generated by Django 3.1.7 on 2021-07-25 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0016_auto_20210725_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photovoltaic',
            name='direction',
            field=models.CharField(choices=[('West', 'West'), ('South', 'South'), ('East', 'East'), ('North', 'North')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='photovoltaic',
            name='envelope_selection',
            field=models.CharField(choices=[('East Roof', 'East Roof'), ('South Roof', 'South Roof'), ('North Roof', 'North Roof'), ('West Roof', 'West Roof')], max_length=10, null=True),
        ),
    ]
