# Generated by Django 3.0.5 on 2020-05-01 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covid',
            name='name',
            field=models.CharField(blank=True, max_length=225, null=True, verbose_name='Name'),
        ),
    ]
