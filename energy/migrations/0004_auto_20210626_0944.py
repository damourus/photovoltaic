# Generated by Django 3.1.7 on 2021-06-26 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0003_auto_20210626_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photovoltaic',
            name='direction',
            field=models.CharField(choices=[('West', 'West'), ('North', 'North'), ('East', 'East'), ('South', 'South')], max_length=10),
        ),
        migrations.AlterField(
            model_name='photovoltaic',
            name='envelope_selection',
            field=models.CharField(choices=[('South Roof', 'South Roof'), ('West Roof', 'West Roof'), ('North Roof', 'North Roof'), ('East Roof', 'East Roof')], max_length=10),
        ),
    ]