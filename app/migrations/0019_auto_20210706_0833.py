# Generated by Django 3.2.4 on 2021-07-06 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20210706_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapdata',
            name='author',
            field=models.CharField(blank=True, max_length=225, null=True, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='mapdata',
            name='color',
            field=models.CharField(blank=True, max_length=125, null=True, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='mapdata',
            name='condition',
            field=models.CharField(blank=True, max_length=625, null=True, verbose_name='Condition'),
        ),
    ]
