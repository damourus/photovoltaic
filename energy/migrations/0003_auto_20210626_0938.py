# Generated by Django 3.1.7 on 2021-06-26 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0002_auto_20210626_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photovoltaic',
            name='b_i_p_v',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], max_length=4),
        ),
        migrations.AlterField(
            model_name='photovoltaic',
            name='direction',
            field=models.CharField(choices=[('South', 'South'), ('East', 'East'), ('North', 'North'), ('West', 'West')], max_length=10),
        ),
        migrations.AlterField(
            model_name='photovoltaic',
            name='envelope_selection',
            field=models.CharField(choices=[('North Roof', 'North Roof'), ('East Roof', 'East Roof'), ('South Roof', 'South Roof'), ('West Roof', 'West Roof')], max_length=10),
        ),
    ]