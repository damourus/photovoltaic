# Generated by Django 3.1.7 on 2021-07-29 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0043_auto_20210729_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photovoltaic',
            name='b_i_p_v',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='photovoltaic',
            name='direction',
            field=models.CharField(choices=[('East', 'East'), ('South', 'South'), ('West', 'West'), ('North', 'North')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='photovoltaic',
            name='envelope_selection',
            field=models.CharField(choices=[('North Roof', 'North Roof'), ('West Roof', 'West Roof'), ('East Roof', 'East Roof'), ('South Roof', 'South Roof')], max_length=10, null=True),
        ),
    ]
