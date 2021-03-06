# Generated by Django 3.0.4 on 2020-03-23 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200312_0753'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='padata',
            options={'ordering': ['price_rate', 'zipcode', 'state', 'plan_type', 'term_length', 'monthly_fee', 'product_last_update']},
        ),
        migrations.AddField(
            model_name='padata',
            name='current_ptc',
            field=models.FloatField(default=0, verbose_name='Current PTC'),
        ),
        migrations.AddField(
            model_name='padata',
            name='future_ptc',
            field=models.FloatField(default=0, verbose_name='Future PTC'),
        ),
        migrations.AddField(
            model_name='padata',
            name='future_ptc_date',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Fureture PTC date'),
        ),
    ]
