# Generated by Django 2.2.5 on 2019-10-10 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challans', '0011_auto_20191009_0353'),
    ]

    operations = [
        migrations.AddField(
            model_name='challan',
            name='is_rates_assigned',
            field=models.BooleanField(default=False),
        ),
    ]
