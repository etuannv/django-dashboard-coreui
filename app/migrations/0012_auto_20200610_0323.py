# Generated by Django 3.0.5 on 2020-06-10 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20200403_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='padata',
            name='fiveh_kwh',
            field=models.FloatField(default=0, verbose_name='500 kWh'),
        ),
        migrations.AddField(
            model_name='padata',
            name='onek_kwh',
            field=models.FloatField(default=0, verbose_name='1000 kWh'),
        ),
        migrations.AddField(
            model_name='padata',
            name='rating',
            field=models.FloatField(default=0, verbose_name='Rating'),
        ),
        migrations.AddField(
            model_name='padata',
            name='twok_kwh',
            field=models.FloatField(default=0, verbose_name='2000 kWh'),
        ),
    ]
