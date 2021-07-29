# Generated by Django 3.1.7 on 2021-07-29 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0041_auto_20210729_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photovoltaic',
            name='direction',
            field=models.CharField(choices=[('East', 'East'), ('South', 'South'), ('West', 'West'), ('North', 'North')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='photovoltaic',
            name='envelope_selection',
            field=models.CharField(choices=[('South Roof', 'South Roof'), ('East Roof', 'East Roof'), ('North Roof', 'North Roof'), ('West Roof', 'West Roof')], max_length=10, null=True),
        ),
    ]
