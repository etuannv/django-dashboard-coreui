# Generated by Django 3.0.4 on 2020-03-23 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200323_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='padata',
            name='future_ptc_date',
            field=models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Fureture PTC date'),
        ),
    ]
