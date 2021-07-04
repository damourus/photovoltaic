# Generated by Django 3.1.7 on 2021-06-29 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0004_auto_20210626_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='photovoltaic',
            name='b_i_p_v',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=4),
        ),
        migrations.AlterField(
            model_name='photovoltaic',
            name='direction',
            field=models.CharField(choices=[('East', 'East'), ('North', 'North'), ('West', 'West'), ('South', 'South')], max_length=10),
        ),
        migrations.AlterField(
            model_name='photovoltaic',
            name='envelope_selection',
            field=models.CharField(choices=[('East Roof', 'East Roof'), ('South Roof', 'South Roof'), ('West Roof', 'West Roof'), ('North Roof', 'North Roof')], max_length=10),
        ),
        migrations.AlterField(
            model_name='radiation',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='energy.location'),
        ),
    ]
